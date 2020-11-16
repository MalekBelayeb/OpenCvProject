import 'dart:convert';
import 'dart:io';

import "package:http/http.dart" as http;
import 'HttpConfig.dart';

class ImageService
{

  Future<http.Response> uploadProfileImage(String route,File file) async
  {
    var url = getServerURL(route, []);

    if(file != null)
    {
      String base64Image = base64Encode(file.readAsBytesSync());

      var response = await http.post(url, body: {
        "image": base64Image,
      });
      //print(respons.body);
      return await response;



    }
  }



}