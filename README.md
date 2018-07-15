# massdl.py
## A simple loop using urllib for downloading files in bulk.

This will work for files that have the same URL with numbers changing.

Cases this could be useful:
 - example.com/archive.rar.part01, example.com/archive.rar.part02...
 - example.com/image.png?id=1, example.com/image.png?id=2...
 - example.com/01/triangle.png, example.com/02/triangle.png...
 - example.com/step1.mp4, example.com/step2.mp4...

 ## How to use
 As an example, let's assume your files are "/image1.png" through "/image23.png".

 In this case, your starting variables should be:
 - `startNum = 1`
 - `stopNum = 23`

 The urllib request should then be as follows:
 ```
 urllib.request.urlretrieve("http://example.com/image" + str(startNum) + ".png", "nameHere" + str(startNum) + ".png")
 ```

 `startNum` is counted like an `i`, so this is what's incrementing each time.

 This would be downloading `http://example.com/image1.png` as `nameHere1.png`, all the way up to 23.