import 'package:flutter/material.dart';

import '../utils/app_theme.dart';

class CustomButton extends StatelessWidget {
  CustomButton({
    Key? key,
    required this.height,
    required this.width,
    this.onPressed,
    this.margin,
    required this.buttonText,
  }) : super(key: key);

  final double height;
  final double width;
  final EdgeInsetsGeometry? margin;
  void Function()? onPressed;
  final String buttonText;

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: onPressed,
      child: Container(
        color: AppTheme.mainFontColor,
        height: height,
        width: width,
        margin: margin ?? EdgeInsets.zero,
        child: Center(
          child: Text(
            buttonText,
            style: const TextStyle(
              fontSize: 16,
              color: AppTheme.whiteColor,
              fontWeight: FontWeight.w400,
            ),
          ),
        ),
      ),
    );
  }
}
