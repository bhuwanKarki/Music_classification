

# --- CONFIGURATIONS FOR Convert_to_wav --- #
class ConvertWav:
    # Path of the song folder which will be used for wav converting
    CONVERT_DIRECTORY = r"C:\Users\minds\Desktop\New\Songs"

    # File extension in song folder
    FILE_TYPE = "mp3"


# --- CONFIGURATIONS FOR Create_Dataset_as_csv --- #
class CreateDataset:
    # Path of GTZAN dataset
    DATASET_DIRECTORY = r"C:\Users\minds\Desktop\New\Songs"

    # Sampling rate (Hz)
    SAMPLING_RATE = 22050

    # Frame size (Samples)
    FRAME_SIZE = 2048

    # Hop Size (Samples)
    HOP_SIZE = 512


class Test:
    # Path for test data
    TEST_DATA_PATH = r"C:\Users\minds\Desktop\New\Songs"

