import os
import subprocess
import tempfile
from flask import Blueprint, request, jsonify, send_file
from werkzeug.utils import secure_filename
from PyPDF2 import PdfReader, PdfWriter

pdf_bp = Blueprint('pdf', __name__)

ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def compress_pdf_pypdf2(input_path, output_path):
    """Compresses a PDF using PyPDF2 (removes blank pages and optimizes content)."""
    try:
        reader = PdfReader(input_path)
        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        with open(output_path, "wb") as f:
            writer.write(f)
        return True, "PyPDF2 compression successful"
    except Exception as e:
        return False, f"Error during PyPDF2 compression: {e}"

def compress_pdf_ghostscript(input_path, output_path, quality='ebook'):
    """Compresses a PDF using Ghostscript with different quality settings."""
    quality_settings = {
        'screen': '/screen',
        'ebook': '/ebook',
        'printer': '/printer',
        'prepress': '/prepress',
        'default': '/default'
    }
    
    if quality not in quality_settings:
        quality = 'ebook'

    command = [
        'gs',
        '-sDEVICE=pdfwrite',
        '-dCompatibilityLevel=1.4',
        '-dPDFSETTINGS={}'.format(quality_settings[quality]),
        '-dNOPAUSE',
        '-dBATCH',
        '-sOutputFile={}'.format(output_path),
        input_path
    ]
    
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return True, "Ghostscript compression successful"
    except subprocess.CalledProcessError as e:
        return False, f"Error during Ghostscript compression: {e.stderr}"
    except FileNotFoundError:
        return False, "Ghostscript not found. Please ensure it is installed."
    except Exception as e:
        return False, f"An unexpected error occurred: {e}"

@pdf_bp.route('/compress', methods=['POST'])
def compress_pdf():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file type. Only PDF files are allowed.'}), 400
    
    method = request.form.get('method', 'ghostscript')
    quality = request.form.get('quality', 'ebook')
    
    # Create temporary files
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_input:
        file.save(temp_input.name)
        input_path = temp_input.name
    
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_output:
        output_path = temp_output.name
    
    try:
        # Get original file size
        original_size = os.path.getsize(input_path)
        
        # Compress the PDF
        if method == 'pypdf2':
            success, message = compress_pdf_pypdf2(input_path, output_path)
        else:
            success, message = compress_pdf_ghostscript(input_path, output_path, quality)
        
        if not success:
            return jsonify({'error': message}), 500
        
        # Get compressed file size
        compressed_size = os.path.getsize(output_path)
        compression_ratio = ((original_size - compressed_size) / original_size) * 100
        
        # Return the compressed file
        return send_file(
            output_path,
            as_attachment=True,
            download_name=f"compressed_{secure_filename(file.filename)}",
            mimetype='application/pdf'
        )
        
    except Exception as e:
        return jsonify({'error': f'Compression failed: {str(e)}'}), 500
    
    finally:
        # Clean up temporary files
        try:
            os.unlink(input_path)
            os.unlink(output_path)
        except:
            pass

@pdf_bp.route('/info', methods=['GET'])
def get_info():
    return jsonify({
        'methods': ['pypdf2', 'ghostscript'],
        'qualities': ['screen', 'ebook', 'printer', 'prepress', 'default'],
        'description': 'PDF Compression Service'
    })

