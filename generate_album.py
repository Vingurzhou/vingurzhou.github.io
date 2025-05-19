import os
import yaml


def generate_album_structure(root_dir, output_file, base_path='album'):
    album_data = {
        'title': '相册',
        'layout': 'album',
        'sections': []
    }

    for subdir in sorted(os.listdir(root_dir)):
        subdir_path = os.path.join(root_dir, subdir)
        if os.path.isdir(subdir_path):
            photos = []
            for filename in sorted(os.listdir(subdir_path)):
                file_path = os.path.join(subdir_path, filename)
                if os.path.isfile(file_path):
                    photos.append(f"{base_path}/{subdir}/{filename}")
            if photos:
                album_data['sections'].append({
                    'title': subdir,
                    'photos': photos
                })
    print(album_data)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('---\n')
        yaml.dump(album_data, f, allow_unicode=True, sort_keys=False)
        f.write('---\n')


if __name__ == "__main__":
    # 修改以下路径为你的目录
    root_directory = 'source/page/album'
    output_markdown = 'source/page/album.md'
    generate_album_structure(root_directory, output_markdown)
