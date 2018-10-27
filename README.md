# pixiv-favotter

Download all your favorite (bookmarked) illusts in [Pixiv](https://www.pixiv.net/)!!

## Tested Environment

+ OS: macOS Sierra
+ python: 3.6.0
+ pixivpy: 3.3.5

## Usage

### Setup

Install [pixivpy](https://github.com/upbit/pixivpy).

```sh
$ pip install pixivpy
($ and something additional depends on your environment)
```

Write your pixiv client info to `client.json`.  
You need `pixiv_id`, `password`, `user_id`

```sh
$ mv client.json.sample client.json
$ vi client.json
```

### Execute

Execute the command bellow, and you can see the images in `images/`.

```sh
$ python pixiv-favotter.py
```
