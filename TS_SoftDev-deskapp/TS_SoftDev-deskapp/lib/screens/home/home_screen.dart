import 'package:fluent_ui/fluent_ui.dart';
import 'package:flutter/material.dart';
import 'package:techshila_pc_client/utils/app_theme.dart';
import 'package:techshila_pc_client/widgets/custom_button.dart';

class HomeScreen extends StatefulWidget {
  HomeScreen({Key? key}) : super(key: key);

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  int _selectedIndex = 0;

  @override
  Widget build(BuildContext context) {
    double height = MediaQuery.of(context).size.height;
    final width = MediaQuery.of(context).size.width;
    height = height - MediaQuery.of(context).padding.top;
    final appBarHieght = AppBar().preferredSize.height;
    return NavigationView(
      appBar: NavigationAppBar(
        title: Text(
          'TechShila',
          style: const TextStyle().copyWith(
            color: AppTheme.blackColor,
            fontWeight: FontWeight.w800,
            fontSize: 20,
          ),
        ),
        backgroundColor: AppTheme.borderColor,
        leading: const Icon(FluentIcons.add_connection,
            color: AppTheme.mainFontColor),
        actions: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Spacer(),
            SizedBox(width: width * 0.025),
            CustomButton(
              suffixIcon:
                  const Icon(FluentIcons.add, color: AppTheme.whiteColor),
              height: appBarHieght,
              onPressed: () {
                print('Clicked - Check');
              },
              width: appBarHieght * 3.5,
              buttonText: 'Add New Device',
            ),
          ],
        ),
      ),
      pane: NavigationPane(
        // header: Icon(FluentIcons.add_connection),
        onChanged: (index) {
          setState(() {
            _selectedIndex = index;
          });
        },
        selected: _selectedIndex,
        items: [
          PaneItem(
            icon: Icon(FluentIcons.home, color: AppTheme.mainFontColor),
            title: Text('Home'),
            body: Text('Home'),
          ),
          PaneItem(
            icon: Icon(FluentIcons.settings, color: AppTheme.mainFontColor),
            title: Text('Settings'),
            body: Text('Settings'),
          ),
        ],
      ),
    );
  }
}
