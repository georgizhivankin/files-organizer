# import PyYAML
import yaml

# Load configuration values from config directory
pathsFile = open("config/paths.yaml", 'r')
fileTypeMapper = open("config/fileTypeMapper.yaml", 'r')
# Process the files with PyYAML
pathsData = yaml.load(pathsFile)
fileTypeData = yaml.load(fileTypeMapper)
print pathsData['scanDirectory']
for targetPath in pathsData['targetPaths']:
    for key, value in targetPath.items():
        category = key
        location = value
        print location
    
    
