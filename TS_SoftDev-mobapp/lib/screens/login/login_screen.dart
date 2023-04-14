import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:techshila/screens/home/bloc/home_bloc.dart';

import '../../widgets/custom_button.dart';
import '../home/home_screen.dart';

class LoginScreen extends StatelessWidget {
  LoginScreen({super.key});
  @override
  Widget build(BuildContext context) {
    double height = MediaQuery.of(context).size.height;
    double width = MediaQuery.of(context).size.width;
    final padding = MediaQuery.of(context).viewPadding;
    height = height - padding.top - padding.bottom;
    return Scaffold(
      appBar: AppBar(
        title: const Text('Login'),
        centerTitle: true,
      ),
      body: Center(
        child: CustomButton(
          width: width * 0.6,
          height: height * 0.08,
          buttonText: 'Login with Google',
          onPressed: () {
            Navigator.pushReplacement(
              context,
              MaterialPageRoute(
                builder: (context) => BlocProvider<HomeScreenBloc>(
                  create: (context) => HomeScreenBloc(),
                  child: const HomeScreen(),
                ),
              ),
            );
          },
        ),
      ),
    );
  }
}
