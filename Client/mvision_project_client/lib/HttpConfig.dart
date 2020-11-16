import 'package:flutter/material.dart';

const String PORT = "5000";
const String DOMAIN = "192.168.1.6";
const String URL = "http://$DOMAIN:$PORT";


String getServerURL(String route,[dynamic data])
{
  String argData = "";
  for(dynamic arg in data)
  {
    if(arg!=null )
    {
      if(arg.toString()!="")
        argData += "/"+ arg.toString();
    }
  }

  route = route + argData;
  route=route.replaceAll('//', '/'); // besh mantihouch fel cas mtaa /users/get//malek

  if(!route.startsWith("/"))        // besh mantihouch fel cas mtaa users/get/malek donc izid just /users/get/malek
      {
    route = "/"+route;
  }


  return URL+route;
}






