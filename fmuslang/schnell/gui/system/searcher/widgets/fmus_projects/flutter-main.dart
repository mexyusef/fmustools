// Importing the Flutter framework
import 'package:flutter/material.dart';

// The main function, starting point of the application
void main() {
  // Runs the app
  runApp(MyApp());
}

// The root widget of the application
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // Material is a predefined visual design language for
    // Android apps. MaterialApp is a pre-built widget in
    // Flutter that follows the Material Design system.
    return MaterialApp(
      title: 'Hello Flutter App',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(),
    );
  }
}

// Home page widget
class MyHomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Hello, Flutter'),
      ),
      body: Center(
        child: Text(
          'Hello, Flutter!',
          style: TextStyle(fontSize: 24.0),
        ),
      ),
    );
  }
}
