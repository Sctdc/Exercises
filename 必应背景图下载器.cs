using System;
using System.Collections.Generic;
using System.Text;
using System.Net;
using System.IO;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

class Program
{
    static void Main(string[] args)
    {
        // 文件名格式为'年_月_日.jpg'
        string picDate = DateTime.Now.Year.ToString() + "_"
                       + DateTime.Now.Month.ToString() + "_"
                       + DateTime.Now.Day.ToString();
        // 获取背景图数据
        string requestUri = @"http://www.bing.com/HPImageArchive.aspx?format=js&mbl=1&idx=0&n=1&video=1";
        var request = WebRequest.Create(requestUri);
        var response = request.GetResponse();
        var respStream = response.GetResponseStream();
        var streamReader = new StreamReader(respStream, Encoding.GetEncoding("utf-8"));
        // 解析背景图下载地址
        var dicts = JsonConvert.DeserializeObject<Dictionary<string, object>>(streamReader.ReadLine());
        var images = (JArray)dicts["images"];
        requestUri = images[0]["url"].ToString();
        // 保存背景图，下载目录为当前目录下/Wallpaper子目录
        var client = new WebClient();
        client.DownloadFile(requestUri, "./Wallpaper/" + picDate + ".jpg");

        Console.WriteLine("今日必应背景图下载完毕！");
    }
}
