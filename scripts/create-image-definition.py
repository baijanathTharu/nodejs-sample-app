import sys
import json

def create_image_definition(file_name, container_name, image_uri):
    image_definition = [{
        "name": container_name,
        "imageUri": image_uri
    }]
    
    with open(file_name, 'w') as f:
        json.dump(image_definition, f)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: create-image-definition.py <output_file> <container_name> <image_uri>")
        sys.exit(1)
    
    output_file = sys.argv[1]
    container_name = sys.argv[2]
    image_uri = sys.argv[3]

    create_image_definition(output_file, container_name, image_uri)
