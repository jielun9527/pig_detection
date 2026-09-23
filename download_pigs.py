from bing_image_downloader import downloader

keywords = [
    "pig farm animal",
    "pig pink animal",
    "pig livestock",
    "猪 养殖场"
]

for kw in keywords:
    downloader.download(
        kw,
        limit=50,
        output_dir='C:/Users/jielun/Desktop/pig_test/pig_dataset/images/train',
        adult_filter_off=True,
        force_replace=False,
        timeout=60
    )
    print(f"{kw} 下载完成")