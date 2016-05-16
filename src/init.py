# import PyYAML
import yaml

# Load configuration values from config directory
fileTypeMapper = open("config/fileTypeMapper.yaml", 'r')
# Process the files with PyYAML
fileTypeData = yaml.load(fileTypeMapper)
# Get all categories of files
for category in fileTypeData['files']:
    print category
    # Get details
    fileData = fileTypeData['files'][category]
    for v in fileData:
        print v
