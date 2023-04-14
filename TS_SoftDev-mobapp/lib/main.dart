import 'package:flutter/material.dart';
import 'package:techshila/screens/home/home_screen.dart';
import 'package:techshila/utils/app_theme.dart';
import 'package:techshila/utils/splash_screen.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Tech-Shila',
      theme: ThemeData.light(useMaterial3: true).copyWith(
        textTheme: ThemeData.light().textTheme.apply(
              fontFamily: 'Cera Pro',
            ),
        primaryTextTheme: ThemeData.light().textTheme.apply(
              fontFamily: 'Cera Pro',
            ),
        scaffoldBackgroundColor: AppTheme.whiteColor,
        focusColor: AppTheme.mainFontColor,
        appBarTheme: const AppBarTheme(
          backgroundColor: AppTheme.whiteColor,
        ),
      ),
      home: const SplashScreen(),
    );
  }
}
