import 'package:flutter/material.dart';

import '../utils/app_theme.dart';

class CustomButton extends StatelessWidget {
  CustomButton({
    Key? key,
    required this.height,
    required this.width,
    this.onPressed,
    this.margin,
    this.suffixIcon,
    required this.buttonText,
  }) : super(key: key);

  final double height;
  final double width;
  final EdgeInsetsGeometry? margin;
  void Function()? onPressed;
  final String buttonText;
  final Icon? suffixIcon;

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
          child: Row(
            children: [
              const SizedBox(width: 15),
              if (suffixIcon != null) suffixIcon!,
              const SizedBox(width: 10),
              Align(
                alignment: Alignment.center,
                child: Text(
                  buttonText,
                  style: const TextStyle(
                    fontSize: 16,
                    color: AppTheme.whiteColor,
                    fontWeight: FontWeight.w400,
                  ),
                ),
              ),
              SizedBox(width: 10),
            ],
          ),
        ),
      ),
    );
  }
}
