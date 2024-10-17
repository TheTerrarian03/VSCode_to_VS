import sys, file_utils, vcx_utils, uuid, os, constants

def are_arguments_valid():
    if len(sys.argv) < 2:
        return False
    if len(sys.argv) >= 2:
        if not file_utils.verify_directory_path(sys.argv[1]):
            return False
    if len(sys.argv) >= 3:
        if not sys.argv[2] in constants.VCX_PROJ_TYPES.keys():
            return False
    
    return True

def get_project_dir_arg():
    if are_arguments_valid():
        return sys.argv[1]
    
def get_project_type_arg():
    if are_arguments_valid():
        if len(sys.argv) >= 3:
            return sys.argv[2]
        else:
            return constants.DEFAULT_PROJ_TYPE

class project_info:
    def __init__(self):
        self.dir = ""
        self.name = ""
        self.proj_type_uuid = ""
        self.proj_unique_uuid = ""
        self.header_files = []
        self.resource_files = []
        self.source_files = []
        self.all_files = []    

    def generate_uuid(self):
        self.proj_unique_uuid = str(uuid.uuid4()).upper()
    
    def generate_main_info(self, project_dir, project_type):
        self.name = os.path.basename(project_dir)
        self.proj_type_uuid = constants.VCX_PROJ_TYPES.get(project_type)
        if self.proj_type_uuid == None:
            raise KeyError("Hey! Invalid type of project given!")
        self.generate_uuid()

    def generate_file_info(self):
        # get details about categorized files
        header_files, resource_files, source_files = file_utils.categorize_files(self.dir)

        # set file info to info about categorized files
        self.header_files = header_files
        self.resource_files = resource_files
        self.source_files = source_files

        # all files
        self.all_files = self.header_files + self.resource_files + self.source_files
