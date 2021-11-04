from kaggle.api.kaggle_api_extended import KaggleApi

if __name__ == '__main__':
    print("Kaggle Data Extractor\n")

    PathForDownload = "C:\\Users\\y84201228\\PycharmProjects\\KaggleApi\\Dataset_Folder"

    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files('kannan1314/innocent-deaths-caused-by-police-all-time', path=PathForDownload, unzip=True)

