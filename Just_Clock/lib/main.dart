import 'package:flutter/material.dart';
import 'package:clock_app_maybe/views/home_view.dart';
import 'package:flutter/services.dart';

void main() {
  // Add these 2 lines
  WidgetsFlutterBinding.ensureInitialized();
  SystemChrome.setEnabledSystemUIOverlays([
    SystemUiOverlay.bottom, //This line is used for showing the bottom bar
  ]);

  runApp(MyApp());
}

class MyApp extends StatefulWidget {
  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      themeMode: ThemeMode.dark,
      theme: ThemeData(
        scaffoldBackgroundColor: Color.fromARGB(115, 48, 44, 44),
      ),
      home: HomeView(),
    );
  }
}
