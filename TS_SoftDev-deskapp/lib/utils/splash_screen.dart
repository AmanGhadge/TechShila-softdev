import 'package:flutter/material.dart';
import 'package:techshila_pc_client/screens/login/login_screen.dart';

import '../screens/home/home_screen.dart';

class SplashScreen extends StatefulWidget {
  const SplashScreen({Key? key}) : super(key: key);

  @override
  State<SplashScreen> createState() => _SplashScreenState();
}

class _SplashScreenState extends State<SplashScreen> {
  @override
  void initState() {
    _navigateToHomeScreen();
    super.initState();
  }

  _navigateToHomeScreen() async {
    await Future.delayed(
      const Duration(
        milliseconds: 1500,
      ),
      () {
        Navigator.pushReplacement(
          context,
          MaterialPageRoute(
            builder: (context) => LoginScreen(),
          ),
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Image.asset(
          'assets/images/appIcon.jpeg',
          fit: BoxFit.contain,
          height: 200,
          width: 200,
          errorBuilder: (context, object, st) {
            return const SizedBox(
              child: Text('Error Occured'),
            );
          },
        ),
      ),
    );
  }
}
