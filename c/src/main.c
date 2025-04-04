#include "common.h"
#include <dirent.h>

void list_subdirectories(const char* base_path) {
    struct dirent* entry;
    DIR* dir = opendir(base_path);

    if (!dir) {
        perror("opendir failed");
        return;
    }

    while ((entry = readdir(dir)) != NULL) {
        if (entry->d_type == DT_DIR && entry->d_name[0] != '.') { // Ignore hidden and special dirs
            char sub_path[1024];
            snprintf(sub_path, sizeof(sub_path), "%s/%s", base_path, entry->d_name);

            DIR* sub_dir = opendir(sub_path);
            if (sub_dir) {
                struct dirent* sub_entry;
                while ((sub_entry = readdir(sub_dir)) != NULL) {
                    if (sub_entry->d_type == DT_DIR && sub_entry->d_name[0] != '.') {
                        printf("%s_%s\n", entry->d_name, sub_entry->d_name);
                    }
                }
                closedir(sub_dir);
            }
        }
    }

    closedir(dir);
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <directory_path>\n", argv[0]);
        return EXIT_FAILURE;
    }

    list_subdirectories(argv[1]);
    return EXIT_SUCCESS;
}
