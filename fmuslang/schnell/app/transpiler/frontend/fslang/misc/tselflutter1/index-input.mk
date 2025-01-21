--% index/fmus
tselflutter1,d(/mk)
	%utama=__FILE__
	main.dart,f(e=utama=/home/usef/common/napaktilas/quat-tsel/tselflutter/lib/main.dart)
	routes.dart,f(e=utama=/home/usef/common/napaktilas/quat-tsel/tselflutter/lib/routes.dart)
	utils.dart,f(e=utama=/home/usef/common/napaktilas/quat-tsel/tselflutter/lib/utils.dart)
	screens,d(/mk)
		login,d(/mk)
			login.dart,f(e=utama=/home/usef/common/napaktilas/quat-tsel/tselflutter/lib/screens/login/login.dart)
		task_list,d(/mk)
			list_weekly.dart,f(e=utama=/home/usef/common/napaktilas/quat-tsel/tselflutter/lib/screens/task_list/list_weekly.dart)
			list_monthly.dart,f(e=utama=/home/usef/common/napaktilas/quat-tsel/tselflutter/lib/screens/task_list/list_monthly.dart)
			list_history.dart,f(e=utama=/home/usef/common/napaktilas/quat-tsel/tselflutter/lib/screens/task_list/list_history.dart)
			list_rejected.dart,f(e=utama=/home/usef/common/napaktilas/quat-tsel/tselflutter/lib/screens/task_list/list_rejected.dart)
			select_category.dart,f(e=utama=/home/usef/common/napaktilas/quat-tsel/tselflutter/lib/screens/task_list/select_category.dart)
			list_daily.dart,f(e=utama=/home/usef/common/napaktilas/quat-tsel/tselflutter/lib/screens/task_list/list_daily.dart)
			select_floor.dart,f(e=utama=/home/usef/common/napaktilas/quat-tsel/tselflutter/lib/screens/task_list/select_floor.dart)
			task_list.dart,f(e=utama=/home/usef/common/napaktilas/quat-tsel/tselflutter/lib/screens/task_list/task_list.dart)
			check_in,d(/mk)
				checkin_list.dart,f(e=utama=/home/usef/common/napaktilas/quat-tsel/tselflutter/lib/screens/task_list/check_in/checkin_list.dart)
				checkin_form.dart,f(e=utama=/home/usef/common/napaktilas/quat-tsel/tselflutter/lib/screens/task_list/check_in/checkin_form.dart)
		navigation,d(/mk)
			custom_tab_bar.dart,f(e=utama=/home/usef/common/napaktilas/quat-tsel/tselflutter/lib/screens/navigation/custom_tab_bar.dart)
			nav_screen.dart,f(e=utama=/home/usef/common/napaktilas/quat-tsel/tselflutter/lib/screens/navigation/nav_screen.dart)
			navigation.dart,f(e=utama=/home/usef/common/napaktilas/quat-tsel/tselflutter/lib/screens/navigation/navigation.dart)
	models,d(/mk)
	components,d(/mk)
		photo_camera,d(/mk)
			photo_camera.dart,f(e=utama=/home/usef/common/napaktilas/quat-tsel/tselflutter/lib/components/photo_camera/photo_camera.dart)
		video_camera,d(/mk)
			video_camera.dart,f(e=utama=/home/usef/common/napaktilas/quat-tsel/tselflutter/lib/components/video_camera/video_camera.dart)
		video_gallery,d(/mk)
			video_gallery.dart,f(e=utama=/home/usef/common/napaktilas/quat-tsel/tselflutter/lib/components/video_gallery/video_gallery.dart)
		layout,d(/mk)
			header_body.dart,f(e=utama=/home/usef/common/napaktilas/quat-tsel/tselflutter/lib/components/layout/header_body.dart)
			layout.dart,f(e=utama=/home/usef/common/napaktilas/quat-tsel/tselflutter/lib/components/layout/layout.dart)
			topbar,d(/mk)
				telkomsel_appbar.dart,f(e=utama=/home/usef/common/napaktilas/quat-tsel/tselflutter/lib/components/layout/topbar/telkomsel_appbar.dart)
			leftbar,d(/mk)
			rightbar,d(/mk)
				rightbar.dart,f(e=utama=/home/usef/common/napaktilas/quat-tsel/tselflutter/lib/components/layout/rightbar/rightbar.dart)
			bottombar,d(/mk)
		photo_gallery,d(/mk)
			photo_gallery.dart,f(e=utama=/home/usef/common/napaktilas/quat-tsel/tselflutter/lib/components/photo_gallery/photo_gallery.dart)
--#

--% /home/usef/common/napaktilas/quat-tsel/tselflutter/lib/main.dart
import 'package:flutter/material.dart';
import 'package:tselflutter/routes.dart';
import './screens/login/login.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      initialRoute: Login.routeName,
      routes: routes,
    );
  }
}


--#

--% /home/usef/common/napaktilas/quat-tsel/tselflutter/lib/routes.dart
import 'package:flutter/widgets.dart';

import './screens/login/login.dart';
import './screens/navigation/nav_screen.dart';

final Map<String, WidgetBuilder> routes = {
  Login.routeName: (context) => Login(),
  // TaskList.routeName: (context) => TaskList(),
  NavScreen.routeName: (context) => NavScreen(),
};

--#

--% /home/usef/common/napaktilas/quat-tsel/tselflutter/lib/utils.dart
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

class Utils {
  static void hideKeyboard(BuildContext context) {
    FocusScopeNode currentFocus = FocusScope.of(context);
    if (!currentFocus.hasPrimaryFocus) {
      currentFocus.unfocus();
    }
  }

  static Future<String> loadAsset() async {
    return await rootBundle.loadString('assets/json/config.json');
  }
}

--#

--% /home/usef/common/napaktilas/quat-tsel/tselflutter/lib/screens/login/login.dart
import 'package:flutter/material.dart';
import 'package:tselflutter/utils.dart';
import 'package:tselflutter/components/layout/layout.dart';

// import 'package:tselflutter/screens/task_list/task_list.dart';
// import '../task_list/task_list.dart';
import '../navigation/nav_screen.dart';

class Login extends StatelessWidget {
  static String routeName = "/login";

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: HeaderBody(
        "Login",
        ElevatedButton(
          style: ElevatedButton.styleFrom(
            primary: Theme.of(context).primaryColor,
          ),
          onPressed: () {
            Utils.hideKeyboard(context);
            Navigator.pushNamed(context, NavScreen.routeName);
          },
          child: Text('Go to Dashboard'),
        ),
      ),
    );
  }
}


--#

--% /home/usef/common/napaktilas/quat-tsel/tselflutter/lib/screens/task_list/list_weekly.dart
import 'package:flutter/material.dart';
import 'package:tselflutter/components/layout/layout.dart';
import 'package:tselflutter/utils.dart';
import '../login/login.dart';

class ListWeekly extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: HeaderBody(
        "Weekly",
        ElevatedButton(
          style: ElevatedButton.styleFrom(
            primary: Theme.of(context).primaryColor,
          ),
          onPressed: () {
            Utils.hideKeyboard(context);
            Navigator.pushNamed(context, Login.routeName);
          },
          child: Text('Go to Login'),
        ),
      ),
    );
  }
}


--#

--% /home/usef/common/napaktilas/quat-tsel/tselflutter/lib/screens/task_list/list_monthly.dart
import 'package:flutter/material.dart';
import 'package:tselflutter/components/layout/layout.dart';
import 'package:tselflutter/utils.dart';
import '../login/login.dart';

class ListMonthly extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: HeaderBody(
        "Monthly",
        ElevatedButton(
          style: ElevatedButton.styleFrom(
            primary: Theme.of(context).primaryColor,
          ),
          onPressed: () {
            Utils.hideKeyboard(context);
            Navigator.pushNamed(context, Login.routeName);
          },
          child: Text('Go to Login'),
        ),
      ),
    );
  }
}


--#

--% /home/usef/common/napaktilas/quat-tsel/tselflutter/lib/screens/task_list/list_history.dart
import 'package:flutter/material.dart';
import 'package:tselflutter/components/layout/layout.dart';
import 'package:tselflutter/utils.dart';
import '../login/login.dart';

class ListHistory extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: HeaderBody(
        "History",
        ElevatedButton(
          style: ElevatedButton.styleFrom(
            primary: Theme.of(context).primaryColor,
          ),
          onPressed: () {
            Utils.hideKeyboard(context);
            Navigator.pushNamed(context, Login.routeName);
          },
          child: Text('Go to Login'),
        ),
      ),
    );
  }
}


--#

--% /home/usef/common/napaktilas/quat-tsel/tselflutter/lib/screens/task_list/list_rejected.dart
import 'package:flutter/material.dart';
import 'package:tselflutter/components/layout/layout.dart';
import 'package:tselflutter/utils.dart';
import '../login/login.dart';

class ListRejected extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: HeaderBody(
        "Rejected",
        ElevatedButton(
          style: ElevatedButton.styleFrom(
            primary: Theme.of(context).primaryColor,
          ),
          onPressed: () {
            Utils.hideKeyboard(context);
            Navigator.pushNamed(context, Login.routeName);
          },
          child: Text('Go to Login'),
        ),
      ),
    );
  }
}


--#

--% /home/usef/common/napaktilas/quat-tsel/tselflutter/lib/screens/task_list/select_category.dart
import 'package:flutter/material.dart';

class SelectCategory extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold();
  }
}


--#

--% /home/usef/common/napaktilas/quat-tsel/tselflutter/lib/screens/task_list/list_daily.dart
import 'package:flutter/material.dart';
import 'package:tselflutter/components/layout/layout.dart';
import 'package:tselflutter/utils.dart';
import '../login/login.dart';

class ListDaily extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: HeaderBody(
        "Daily",
        ElevatedButton(
          style: ElevatedButton.styleFrom(
            primary: Theme.of(context).primaryColor,
          ),
          onPressed: () {
            Utils.hideKeyboard(context);
            Navigator.pushNamed(context, Login.routeName);
          },
          child: Text('Go to Login'),
        ),
      ),
    );
  }
}


--#

--% /home/usef/common/napaktilas/quat-tsel/tselflutter/lib/screens/task_list/select_floor.dart
import 'package:flutter/material.dart';

class SelectFloor extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold();
  }
}

--#

--% /home/usef/common/napaktilas/quat-tsel/tselflutter/lib/screens/task_list/task_list.dart
export 'list_daily.dart';
export 'list_history.dart';
export 'list_monthly.dart';
export 'list_rejected.dart';
export 'list_weekly.dart';

--#

--% /home/usef/common/napaktilas/quat-tsel/tselflutter/lib/screens/task_list/check_in/checkin_list.dart
import 'package:flutter/material.dart';

class CheckinList extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold();
  }
}



--#

--% /home/usef/common/napaktilas/quat-tsel/tselflutter/lib/screens/task_list/check_in/checkin_form.dart
import 'package:flutter/material.dart';

class CheckinForm extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold();
  }
}


--#

--% /home/usef/common/napaktilas/quat-tsel/tselflutter/lib/screens/navigation/custom_tab_bar.dart
import 'package:flutter/material.dart';

class CustomTabBar extends StatelessWidget {
  final List<IconData> icons;
  final int selectedIndex;
  final Function(int) onTap;

  const CustomTabBar({
    Key key,
    @required this.icons,
    @required this.selectedIndex,
    @required this.onTap,
  }): super(key:key);

  @override
  Widget build(BuildContext context) {
    return TabBar(
      indicatorPadding: EdgeInsets.zero,
      indicator: BoxDecoration(
        border: Border(
          top: BorderSide(
            color: Colors.blueAccent,
            width: 3.0,
          ),
        )
      ),
      tabs: icons
        .asMap()
        .map((index, item) =>
          MapEntry(index, Tab(
              icon: Icon(
                item,
                color: index==selectedIndex ? Colors.blueAccent : Colors.black12,
                size: 30.0,
              ),
            ),
          )
        )
        .values
        .toList(),
    );
  }
}


--#

--% /home/usef/common/napaktilas/quat-tsel/tselflutter/lib/screens/navigation/nav_screen.dart
import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:material_design_icons_flutter/material_design_icons_flutter.dart';
// import 'package:tselflutter/utils.dart';
import 'package:tselflutter/screens/task_list/task_list.dart';
import 'custom_tab_bar.dart';

class _NavScreenState extends State<NavScreen> {

  final List<String> menu_titles = [
    "Daily",
    "Weekly",
    "Monthly",
    "Rejected",
    "History"
  ];
  final List<IconData> menu_icons = [
    Icons.home,
    Icons.ondemand_video,
    Icons.menu,
    MdiIcons.accountCircleOutline,
    MdiIcons.bellOutline
  ];
  final List<Widget> screens = [
    ListDaily(),
    ListWeekly(),
    ListMonthly(),
    ListRejected(),
    ListHistory(),
  ];
  int _selectedIndex = 0;
  
  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      // length: widget.menu_titles.length,
      length: menu_titles.length,
      child: Scaffold(
        // body: widget.screens[_selectedIndex],
        body: TabBarView(
          physics: NeverScrollableScrollPhysics(),
          // children: widget.screens,
          children: screens,
        ),
        // body: IndexedStack(
        //   index: _selectedIndex,
        //   // children: widget.screens,
        //   children: screens,
        // ),
        bottomNavigationBar: Padding(
          padding: const EdgeInsets.only(bottom: 12.0),
          child: CustomTabBar(
            // icons: widget.menu_icons,
            icons: menu_icons,
            selectedIndex: _selectedIndex,
            onTap: (index) => setState(()=>_selectedIndex=index),
          ),
        ),
      ),
    );
  }
}

class NavScreen extends StatefulWidget {
  static String routeName = "/nav-screen";

  NavScreen({Key key, this.title}) : super(key: key);
  // {
  //   Utils.loadAsset()
  //       .then((value) {
  //     String nilai = json.decode(value);
  //     menu_titles.add(nilai);
  //   });
  // }

  final String title;



  @override
  _NavScreenState createState() => _NavScreenState();
}


--#

--% /home/usef/common/napaktilas/quat-tsel/tselflutter/lib/screens/navigation/navigation.dart
export 'nav_screen.dart';
--#

--% /home/usef/common/napaktilas/quat-tsel/tselflutter/lib/components/photo_camera/photo_camera.dart

--#

--% /home/usef/common/napaktilas/quat-tsel/tselflutter/lib/components/video_camera/video_camera.dart

--#

--% /home/usef/common/napaktilas/quat-tsel/tselflutter/lib/components/video_gallery/video_gallery.dart

--#

--% /home/usef/common/napaktilas/quat-tsel/tselflutter/lib/components/layout/header_body.dart
import 'package:flutter/material.dart';
class HeaderBody extends StatelessWidget {
  final String title;
  final Widget body_component;
  HeaderBody(
    @required this.title,
    @required this.body_component,
  );

  @override
  Widget build(BuildContext context) {
    return CustomScrollView(
      slivers: [
        SliverAppBar(
          brightness: Brightness.light,
          backgroundColor: Colors.white,
          title: Text(
            title,
            style: TextStyle(
              color: Colors.blueAccent,
              fontSize: 28.0,
              fontWeight: FontWeight.bold,
              letterSpacing: -1.2,
            ),
          ),
          floating: true,
          actions: [
            Container(
              margin: EdgeInsets.all(6.0),
              decoration: BoxDecoration(
                color: Colors.grey[200],
                shape: BoxShape.circle,
              ),
              child: IconButton(
                  icon: Icon(Icons.search),
                  iconSize: 30.0,
                  // color: Colors.black,
                  onPressed: (){}
              ),
            ),
          ],
        ),
        SliverToBoxAdapter(
          child: Container(
            child: body_component,
          ),
        ),
      ],
    );
  }
}


--#

--% /home/usef/common/napaktilas/quat-tsel/tselflutter/lib/components/layout/layout.dart
export './topbar/telkomsel_appbar.dart';
export 'header_body.dart';
--#

--% /home/usef/common/napaktilas/quat-tsel/tselflutter/lib/components/layout/topbar/telkomsel_appbar.dart
import 'package:flutter/material.dart';

class TelkomselAppBar extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return SliverAppBar(
      brightness: Brightness.light,
      backgroundColor: Colors.white,
      title: Text(
        'Audit DC',
        style: TextStyle(
          color: Colors.blueAccent,
          fontSize: 28.0,
          fontWeight: FontWeight.bold,
          letterSpacing: -1.2,
        ),
      ),
      floating: true,
      actions: [
        Container(
          margin: EdgeInsets.all(6.0),
          decoration: BoxDecoration(
            color: Colors.grey[200],
            shape: BoxShape.circle,
          ),
          child: IconButton(
              icon: Icon(Icons.search),
              iconSize: 30.0,
              // color: Colors.black,
              onPressed: (){}
          ),
        ),
      ],
    );
  }
}


--#

--% /home/usef/common/napaktilas/quat-tsel/tselflutter/lib/components/layout/rightbar/rightbar.dart
import 'package:flutter/material.dart';

class Rightbar extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold();
  }
}

--#

--% /home/usef/common/napaktilas/quat-tsel/tselflutter/lib/components/photo_gallery/photo_gallery.dart

--#