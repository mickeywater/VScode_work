读取用户提供的文件夹中的md文件，把每个{x}个子主题的内容，按如下json格式进行输出，然后将输出的结果另存为`子主题.json` 文件中。
```json
{
  "子主题": {
    "主题": "Your Windows 11 PC has been updated",
    "子主题": "Discover 5 features to help you get more from your device",
    "内容图片": "页面中左侧的粉红色部分",
    "内容文本主题": "Your second set of eyes",
    "内容文本内容": "Activate Copilot Vision on Windows for helpful summaries, to translate texts, or decipher images. Share your browser or an app. Copilot can help with whatever you're working on and even coach you through it aloud."
  }
}
```
当你准备好了，提示用户输入文件夹。