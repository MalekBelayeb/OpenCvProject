
import 'package:flutter/material.dart';
import 'package:mvision_project_client/HomeScreen.dart';



void main() => runApp(App());

class App extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Title',
      home: HomeScreen(),
    );
  }
}