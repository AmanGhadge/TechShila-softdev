import 'package:flutter/material.dart';
import 'package:techshila/widgets/custom_textfield.dart';

import '../../utils/app_theme.dart';
import '../../widgets/custom_button.dart';

class ConnectScreen extends StatelessWidget {
  ConnectScreen({super.key});
  final TextEditingController _ipAddressController = TextEditingController();
  @override
  Widget build(BuildContext context) {
    double height = MediaQuery.of(context).size.height;
    double width = MediaQuery.of(context).size.width;
    final padding = MediaQuery.of(context).viewPadding;
    height = height - padding.top - padding.bottom;
    return Scaffold(
      appBar: AppBar(
        title: const Text('Tech-Shila'),
        centerTitle: true,
        leading: IconButton(
          onPressed: () {
            Navigator.pop(context);
          },
          icon: const Padding(
            padding: EdgeInsets.symmetric(
              horizontal: 20,
            ),
            child: Icon(
              Icons.arrow_circle_left,
              size: 40,
              color: AppTheme.blackColor,
            ),
          ),
        ),
      ),
      body: SingleChildScrollView(
        child: SizedBox(
          height: height * 0.93,
          width: width,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.start,
            children: [
              SizedBox(
                height: height * 0.05,
              ),
              SizedBox(
                width: width * 0.6,
                child: CustomTextField(
                  label: 'Enter IP Address',
                  controller: _ipAddressController,
                ),
              ),
              SizedBox(
                height: height * 0.1,
              ),
              const Text(
                'Or',
                style: TextStyle(
                  color: AppTheme.blackColor,
                ),
              ),
              SizedBox(
                height: height * 0.1,
              ),
              SizedBox(
                width: width * 0.6,
                child: CustomTextField(
                  label: 'Enter Computer Name',
                  controller: _ipAddressController,
                ),
              ),
              SizedBox(
                height: height * 0.05,
              ),
              SizedBox(
                width: width * 0.6,
                child: CustomTextField(
                  label: 'Enter Password',
                  controller: _ipAddressController,
                ),
              ),
              const Spacer(),
              CustomButton(
                height: height * 0.08,
                width: width,
                onPressed: () {},
                buttonText: 'Connect',
              ),
            ],
          ),
        ),
      ),
    );
  }
}
