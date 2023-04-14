import 'package:flutter/material.dart';
import 'package:techshila/utils/app_theme.dart';

class CustomTextField extends StatelessWidget {
  CustomTextField({
    required this.label,
    required this.controller,
    this.validator,
  });

  final String label;
  String? Function(String?)? validator;
  final TextEditingController controller;

  @override
  Widget build(BuildContext context) {
    return TextFormField(
      decoration: InputDecoration(
        labelText: label,
        floatingLabelAlignment: FloatingLabelAlignment.center,
        fillColor: AppTheme.mainFontColor,
        filled: true,
        errorStyle: const TextStyle(color: AppTheme.firstColor),
        labelStyle: const TextStyle(color: AppTheme.whiteColor),
        errorBorder: const UnderlineInputBorder(
          borderSide: BorderSide(color: Colors.red),
        ),
        focusedErrorBorder: const UnderlineInputBorder(
          borderSide: BorderSide(color: AppTheme.borderColor),
        ),
        enabledBorder: const UnderlineInputBorder(
          borderSide: BorderSide(color: AppTheme.firstColor),
        ),
        focusedBorder: const UnderlineInputBorder(
          borderSide: BorderSide(color: AppTheme.firstColor),
        ),
      ),
      style: const TextStyle(color: AppTheme.whiteColor),
      maxLines: 1,
      controller: controller,
      validator: validator,
    );
  }
}
