import 'package:flutter/material.dart';
import 'package:techshila_pc_client/widgets/custom_textfield.dart';

import '../../utils/app_theme.dart';
import '../../widgets/custom_button.dart';
import '../home/home_screen.dart';

class LoginScreen extends StatelessWidget {
  LoginScreen({super.key});
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();
  @override
  Widget build(BuildContext context) {
    double height = MediaQuery.of(context).size.height;
    double width = MediaQuery.of(context).size.width;
    final padding = MediaQuery.of(context).viewPadding;
    height = height - padding.top - padding.bottom;
    final GlobalKey<FormState> _formKey = GlobalKey();
    return Scaffold(
      appBar: AppBar(
        title: const Text('Login'),
        backgroundColor: AppTheme.mainFontColor,
        centerTitle: true,
      ),
      body: SizedBox(
        height: height,
        child: Center(
          child: Form(
            key: _formKey,
            child: SizedBox(
              width: width * 0.6,
              height: height * 0.8,
              child: Column(
                children: [
                  CustomTextField(
                    label: 'Enter Email',
                    controller: _emailController,
                    validator: (value) {
                      if (value != null) {
                        return 'Please enter valid email address.';
                      }
                      return '';
                    },
                  ),
                  SizedBox(
                    height: height * 0.02,
                  ),
                  CustomTextField(
                    label: 'Enter Password',
                    controller: _passwordController,
                    validator: (value) {
                      if (value != null) {
                        return 'Please enter valid password.';
                      }
                      return '';
                    },
                    isObsecureText: true,
                  ),
                  SizedBox(
                    height: height * 0.02,
                  ),
                  CustomButton(
                    height: height * 0.1,
                    width: width * 0.3,
                    buttonText: 'Login',
                    onPressed: () {
                      if (_formKey.currentState!.validate()) {
                        Navigator.pushReplacement(
                            context,
                            MaterialPageRoute(
                                builder: (context) => HomeScreen()));
                      }
                    },
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}
