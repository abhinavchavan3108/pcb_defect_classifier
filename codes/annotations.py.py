# annotations.py

import pandas as pd
import xml.etree.ElementTree as ET
import os


# SET YOUR LOCAL ROOT DIRECTORY
root_dir = r'C:\Users\abhin\OneDrive\Documents\python programs\PCB_defect_detection'
dataset_dir = os.path.join(root_dir, 'PCB_DATASET')
annot_dir = os.path.join(dataset_dir, 'Annotations')


def parse_xml(xml_file):
    """Parse XML annotation file and extract bounding box data."""
    tree = ET.parse(xml_file)
    root = tree.getroot()
    data = []

    filename = root.find('filename').text
    width = int(root.find('size/width').text)
    height = int(root.find('size/height').text)

    for obj in root.findall('object'):
        name = obj.find('name').text
        xmin = int(obj.find('bndbox/xmin').text)
        ymin = int(obj.find('bndbox/ymin').text)
        xmax = int(obj.find('bndbox/xmax').text)
        ymax = int(obj.find('bndbox/ymax').text)

        data.append({
            'filename': filename,
            'width': width,
            'height': height,
            'class': name,
            'xmin': xmin,
            'ymin': ymin,
            'xmax': xmax,
            'ymax': ymax
        })

    return data


def load_all_annotations(annot_dir):
    """Load all XML annotations from directory and subdirectories."""
    # List to store parsed data from all XML files
    all_data = []

    # Recursively traverse subdirectories
    for root, dirs, files in os.walk(annot_dir):
        for name in files:
            if name.endswith('.xml'):
                xml_path = os.path.join(root, name)
                try:
                    all_data.extend(parse_xml(xml_path))
                except Exception as e:
                    print(f"Error parsing {xml_path}: {e}")

    # Create DataFrame from the parsed data
    annot_df = pd.DataFrame(all_data)
    return annot_df


if __name__ == "__main__":
    # Verify paths exist
    print(f"Annotations directory: {annot_dir}")
    print(f"Directory exists: {os.path.exists(annot_dir)}\n")
    
    if not os.path.exists(annot_dir):
        print("ERROR: Annotations directory does not exist!")
        exit()
    
    # Load all annotations
    print("Loading annotations...")
    annot_df = load_all_annotations(annot_dir)
    
    # Display results
    print(f"\nTotal annotations loaded: {len(annot_df)}")
    print(f"\nDataFrame shape: {annot_df.shape}")
    print("\nFirst few rows:")
    print(annot_df.head())
    
    # Display class distribution
    print("\nClass distribution:")
    print(annot_df['class'].value_counts())
    
    # Optional: Save to CSV
    output_path = os.path.join(root_dir, 'annotations_data.csv')
    annot_df.to_csv(output_path, index=False)
    print(f"\nAnnotations saved to: {output_path}")