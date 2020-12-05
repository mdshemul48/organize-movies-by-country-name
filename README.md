# _Organize movies by country name_

This script will make you directory look like.

#### This
```
Old Movie Folder:.
|   The Legend of Tomiris (2019) 1080p BluRay Kazakh H264.mp4
|   
+---A Moon of Nickel and Ice (2017) 1080p AMZN WEBRip DDP 2.0 French x264 ESub
|       A Moon of Nickel and Ice (2017) 1080p AMZN WEBRip DDP 2.0 French x264 ESub.mkv
|       
\---Cold.Prey.2.2008.NORWEGIAN.1080p.BluRay.H264.AAC-VXT
        Cold.Prey.2.2008.NORWEGIAN.1080p.BluRay.H264.AAC-VXT.mp4
```
### to 
```
New Movie Folder:.
|  
+---Canada
|   \---A Moon of Nickel and Ice (2017) 1080p Web H.264
|           A Moon of Nickel and Ice (2017) 1080p AMZN WEBRip DDP 2.0 French x264 ESub.mkv
|           
+---Kazakhstan
|   \---The Legend of Tomiris (2019) 1080p Blu-ray H.264
|           The Legend of Tomiris (2019) 1080p BluRay Kazakh H264.mp4
|           
\---Norway
    \---Cold Prey 2 (2008) 1080p Blu-ray H.264
            Cold.Prey.2.2008.NORWEGIAN.1080p.BluRay.H264.AAC-VXT.mp4
```
You can test this using given folder in this Repository folder called test.

In order to do that, You need to have Python and PIP installed on your system. 

First download the Repository. Then open CMD on that folder. 

```sh
$ pip install requirements.txt
```

You all set!

Now open the main.py file and provide the required information there.

Thank You.