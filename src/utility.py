from PIL import Image
import pytesseract
import re
from io import BytesIO

def extract_text_from_image(image):
    """
    Extracts text from an image file.
    
    Parameters:
    - image: An image file opened with PIL.
    
    Returns:
    - extracted_text (str): Text extracted from the image.
    """
    extracted_text = pytesseract.image_to_string(image)
    return extracted_text

def remove_words_from_text(text, words_to_remove):
    """
    Removes all instances of specified words from the text, case-insensitively.
    
    Parameters:
    - text (str): The original text.
    - words_to_remove (list of str): Words to remove from the text.
    
    Returns:
    - modified_text (str): Text with specified words removed.
    """
    for word in words_to_remove:
        # Remove each word as a standalone word, ignoring case
        word_pattern = rf"\b{re.escape(word.strip())}\b"
        text = re.sub(word_pattern, "", text, flags=re.IGNORECASE)
    # Remove any extra whitespace resulting from removals
    modified_text = re.sub(r'\s+', ' ', text).strip()
    return modified_text