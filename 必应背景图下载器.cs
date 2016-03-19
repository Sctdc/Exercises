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
        string requestUri = @"http://www.bing.com/HPImageArchive.aspx?format=js&mbl=1&idx=0&n=1&video=1";
        string picDate;
        var dicts = new Dictionary<string, object>();

        try
        {
            var request = WebRequest.Create(requestUri);
            var response = request.GetResponse();
            var respStream = response.GetResponseStream();
            var streamReader = new StreamReader(respStream, Encoding.GetEncoding("utf-8"));
            dicts = JsonConvert.DeserializeObject<Dictionary<string, object>>(streamReader.ReadLine());
        }
        catch (Exception)
        {
            Console.WriteLine("获取背景图信息出错！按任意键退出......");
            Console.ReadKey();
            goto Exit;
        }

        try
        {
            var images = (JArray)dicts["images"];
            picDate = images[0]["startdate"].ToString();
            requestUri = images[0]["url"].ToString();
        }
        catch (Exception)
        {
            Console.WriteLine("解析背景图信息出错！按任意键退出......");
            Console.ReadKey();
            goto Exit;
        }

        try
        {
            var client = new WebClient();
            client.DownloadFile(requestUri, "./Wallpaper/" + picDate + ".jpg");
        }
        catch (Exception)
        {
            Console.WriteLine("保存背景图出错！按任意键退出......");
            Console.ReadKey();
            goto Exit;
        }

        Console.WriteLine("今日必应背景图下载完毕！");

    Exit:;
    }
}
