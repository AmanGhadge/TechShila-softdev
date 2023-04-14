import 'package:flutter/material.dart';
import '../../utils/app_theme.dart';
import '../../widgets/custom_button.dart';

class DashboardScreen extends StatelessWidget {
  const DashboardScreen({super.key});
  @override
  Widget build(BuildContext context) {
    double height = MediaQuery.of(context).size.height;
    double width = MediaQuery.of(context).size.width;
    final padding = MediaQuery.of(context).viewPadding;
    height = height - padding.top - padding.bottom;
    return Scaffold(
      appBar: AppBar(
        title: Column(
          children: const [
            Text('Computer One'),
            Text('192.1.0.xx'),
          ],
        ),
        centerTitle: true,
      ),
      body: SingleChildScrollView(
        child: SizedBox(
          height: height,
          width: width,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.start,
            children: [
              SizedBox(
                height: height * 0.05,
              ),
              CustomButton(
                height: height * 0.08,
                onPressed: () {},
                width: width * 0.4,
                buttonText: 'Shutdown',
              ),
              SizedBox(
                height: height * 0.05,
              ),
              CustomButton(
                height: height * 0.08,
                width: width * 0.4,
                onPressed: () {},
                buttonText: 'Sleep',
              ),
              SizedBox(
                height: height * 0.05,
              ),
              const Text(
                'Tasks Running',
                style: TextStyle(
                  color: AppTheme.blackColor,
                  fontWeight: FontWeight.w400,
                  fontSize: 20,
                ),
              ),
              SizedBox(
                height: height * 0.05,
              ),
              SingleChildScrollView(
                child: SizedBox(
                  height: height * 0.5,
                  width: width * 0.9,
                  child: ListView.builder(
                    itemCount: 10,
                    itemBuilder: (context, index) {
                      return Padding(
                        padding: EdgeInsets.symmetric(vertical: height * 0.01),
                        child: Container(
                          color: AppTheme.borderColor,
                          child: ListTile(
                            title: const Text('Task 1'),
                            trailing: IconButton(
                              onPressed: () {},
                              icon: const Icon(
                                Icons.close_outlined,
                                color: AppTheme.blackColor,
                              ),
                            ),
                          ),
                        ),
                      );
                    },
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
