
import 'package:flutter/material.dart';
import 'dart:io';

import 'package:image_picker/image_picker.dart';
import 'package:mvision_project_client/ImageController.dart';
import 'package:mvision_project_client/ImageService.dart';
import "package:http/http.dart" as http;

class HomeScreen extends StatefulWidget {
  ImageService imgservice = ImageService();

  HomeScreen();
  @override
  HomeScreenState createState() => HomeScreenState();

}

class HomeScreenState extends State<HomeScreen>
{
  bool send_card = false;
  File _image_card = null;

  bool send_diploma = false;
  File _image_diploma = null;

  String message_response="";
  ImageController imageController = ImageController();
  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      initialIndex: 0,
      length: 2,
      child: Scaffold(
        appBar: AppBar(
            title: Center(child: Text("Info Verifier")),
            bottom: TabBar(
              isScrollable: true,
              labelColor: Colors.red,
              indicatorColor: Colors.white60,
              unselectedLabelColor: Colors.black,
              tabs: [
                Padding(
                  padding: const EdgeInsets.only(
                      top: 8.0, bottom: 8.0, right: 8.0),
                  child: Text("Photo Verification"),
                ),

                Padding(
                  padding: const EdgeInsets.only(
                      top: 8.0, bottom: 8.0, right: 8.0),
                  child: Text("Diploma Verification"),
                )
              ],
            ),
        ),

        body: TabBarView(

        children: [
          Container(

            child:_photoVerification() ,
          ),
          Container(

            child:_diplomaVerification() ,
          )
        ],
        ),
      ),

    );

  }




  _photoVerification()
  {
   return SingleChildScrollView(

      child: Column(

        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Container(padding: EdgeInsets.only(top:50), height: 100,child: Text("Please upload a card photo and press send",style: TextStyle(fontSize: 18,color: Colors.purpleAccent),) ,),
          Card(
            child: new Container(

              child:_image_card ==null ? Container(width: 300, height: 300) : Image.file(_image_card, width: 300,
                height: 300,
                fit: BoxFit.fitHeight,) ,

              decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  color: Colors.transparent,
                  border: Border.all(width: 1.0, color: Colors.transparent)),
            ),

          ),

          (send_card && _image_card !=null) ? FutureBuilder(

            future: widget.imgservice.uploadProfileImage("/getimage", _image_card),
            builder: (context,snapshot){

              if(snapshot.hasData)
              {
                send_card = false;
                var response = snapshot.data as http.Response;
                print(response.body);

                if(response.body == "NO_CARD_FACE")
                {
                  this.message_response = "No Face Detected On IdCard Please Retry";
                  return Center(

                    child: Text(this.message_response,style: TextStyle(fontSize: 20,color: Colors.red)),

                  );
                }else{

                  if(response.body == "NOT_SIMILAR")
                    {
                      this.message_response = "Similarity: "+response.body;

                    }else{
                    this.message_response = "Similarity: "+response.body+" %";

                  }

                  return Center(

                    child: Text(this.message_response,style: TextStyle(fontSize: 20,color: Colors.purpleAccent)),

                  );
                }



              }else{
                return CircularProgressIndicator();
              }

            },


          ):Container(),
          /* Card(

              child: new Container(

                child:_image ==null ? Container() :
                FutureBuilder(
                  future: imageController.filterCardImage(_image),
                  builder: (context, snapshot){

                    print(snapshot.hasData);

                    if(snapshot.hasData)
                    {
                      return Image.file(snapshot.data, width: 200,
                        height: 200,
                        fit: BoxFit.fitHeight,);
                    }else{

                      return Container();

                    }


                  },


                ) ,

              ),

            ),*/
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [

              RaisedButton(
                child: Icon(
                  Icons.camera_alt,
                  color: Colors.purpleAccent,
                ),

                onPressed: () {

                  AskIfGalleryOrCameraForCard(context);

                },
              ),
              RaisedButton(

                child: Icon(
                  Icons.call_made,
                  color: Colors.purpleAccent,
                ),

                onPressed: () {

                  setState(() {
                    send_card = true;
                  });
                  //imgservice.uploadProfileImage("/getimage",  _image);

                },
              )

            ],
          ),



        ],

      ),
    );
  }



  _diplomaVerification()
  {
    return SingleChildScrollView(

      child: Column(

        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Container(padding: EdgeInsets.only(top:50), height: 100,child: Text("Please upload a diploma photo and press send",style: TextStyle(fontSize: 18,color: Colors.lightGreen),) ,),
          Card(
            child: new Container(

              child:_image_diploma ==null ? Container(width: 300, height: 300) : Image.file(_image_diploma, width: 300,
                height: 300,
                fit: BoxFit.fitHeight,) ,

              decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  color: Colors.transparent,
                  border: Border.all(width: 1.0, color: Colors.transparent)),
            ),

          ),

          (send_diploma && _image_diploma !=null) ? FutureBuilder(

            future: widget.imgservice.uploadProfileImage("/getdiploma", _image_diploma),
            builder: (context,snapshot){

              if(snapshot.hasData)
              {
                send_diploma = false;
                var response = snapshot.data as http.Response;
                print(response.body);

                if(response.body == "IMG_NOT_CLEAR")
                {

                  this.message_response = "Diploma photo is not clear Please Retry";
                  return Center(

                    child: Text(this.message_response,style: TextStyle(fontSize: 20,color: Colors.red)),

                  );
                }else{

                  this.message_response = "Similarity: "+response.body+" %";
                  return Center(

                    child: Text(this.message_response,style: TextStyle(fontSize: 22,color: Colors.lightGreen)),

                  );
                }



              }else{
                return CircularProgressIndicator();
              }

            },


          ):Container(),
          /* Card(

              child: new Container(

                child:_image ==null ? Container() :
                FutureBuilder(
                  future: imageController.filterCardImage(_image),
                  builder: (context, snapshot){

                    print(snapshot.hasData);

                    if(snapshot.hasData)
                    {
                      return Image.file(snapshot.data, width: 200,
                        height: 200,
                        fit: BoxFit.fitHeight,);
                    }else{

                      return Container();

                    }


                  },


                ) ,

              ),

            ),*/
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [

              RaisedButton(
                child: Icon(
                  Icons.camera_alt,
                  color: Colors.lightGreen,
                ),

                onPressed: () {

                  AskIfGalleryOrCameraForDiploma(context);

                },
              ),
              RaisedButton(

                child: Icon(
                  Icons.call_made,
                  color: Colors.lightGreen,
                ),

                onPressed: () {

                  setState(() {
                    send_diploma = true;
                  });
                  //imgservice.uploadProfileImage("/getimage",  _image);

                },
              )

            ],
          ),



        ],

      ),
    );
  }

  _imgFromCameraForCard() async {

    File image = await ImagePicker.pickImage(
        source: ImageSource.camera, imageQuality: 50);

    setState(() {
      _image_card = image;
    });
  }

  _imgFromGalleryForCard() async {
    File image = await ImagePicker.pickImage(
        source: ImageSource.gallery, imageQuality: 50);

    setState(() {
      _image_card = image;
    });
  }

  void AskIfGalleryOrCameraForCard(context) {
    showModalBottomSheet(
        context: context,
        builder: (BuildContext bc) {
          return SafeArea(
            child: Container(
              child: new Wrap(
                children: <Widget>[
                  new ListTile(
                      leading: new Icon(Icons.photo_library),
                      title: new Text('Gallery'),
                      onTap: () {
                        _imgFromGalleryForCard();
                        Navigator.of(context).pop();
                      }),
                  new ListTile(
                    leading: new Icon(Icons.photo_camera),
                    title: new Text('Camera'),
                    onTap: () {
                      _imgFromCameraForCard();
                      Navigator.of(context).pop();
                    },
                  ),
                ],
              ),
            ),
          );
        });
  }



  _imgFromCameraForDiploma() async {

    File image = await ImagePicker.pickImage(
        source: ImageSource.camera, imageQuality: 50);

    setState(() {
      _image_diploma = image;
    });
  }

  _imgFromGalleryForDiploma() async {
    File image = await ImagePicker.pickImage(
        source: ImageSource.gallery, imageQuality: 50);

    setState(() {
      _image_diploma = image;
    });
  }

  void AskIfGalleryOrCameraForDiploma(context) {
    showModalBottomSheet(
        context: context,
        builder: (BuildContext bc) {
          return SafeArea(
            child: Container(
              child: new Wrap(
                children: <Widget>[
                  new ListTile(
                      leading: new Icon(Icons.photo_library),
                      title: new Text('Gallery'),
                      onTap: () {
                        _imgFromGalleryForDiploma();
                        Navigator.of(context).pop();
                      }),
                  new ListTile(
                    leading: new Icon(Icons.photo_camera),
                    title: new Text('Camera'),
                    onTap: () {
                      _imgFromCameraForDiploma();
                      Navigator.of(context).pop();
                    },
                  ),
                ],
              ),
            ),
          );
        });
  }



}