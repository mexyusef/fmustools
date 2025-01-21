--% rujukan
https://www.lihaoyi.com/post/ScrapingWebsitesusingScalaandJsoup.html

http://www.scalafx.org/docs/faq_TableView_with_Custom_cell/
https://github.com/scalafx/scalafx/tree/master/scalafx-demos/src/main/scala/scalafx/controls/tableview

-- create stage
  stage = new PrimaryStage {
    scene = new Scene(800, 600) {
      // ini butuh di build.sbt
      // resourceDirectory in Compile := baseDirectory(_ / "src").value
      // agar resource dicopy ke classes/
      stylesheets = List(getClass.getResource(filecss).toExternalForm)
      root = new BorderPane {
        top = new VBox {
          children = List(
            createMenus(),
            createToolBar()
          )
          center = createTabs()
        }
      }
    }
    title = "Aplikasi ScalaFX jaman now!"
  }
-- create tabs
  private def createTabs(): TabPane = {
    new TabPane {
      tabs = List(
        new Tab {
          text = "TableView"
          content = createTableDemoNode()
          closable = false
        },
      )
    }
  }
-- create table view

  private def createTableDemoNode(): Node = {
    // Create columns
    val firstNameColumn = new TableColumn[Person, String] {
      text = "First Name"
      cellValueFactory = {
        _.value.firstName
      }
      prefWidth = 180
    }
    val lastNameColumn = new TableColumn[Person, String] {
      text = "Last Name"
      cellValueFactory = {
        _.value.lastName
      }
      prefWidth = 180
    }
    val phoneColumn = new TableColumn[Person, String] {
      text = "Phone"
      cellValueFactory = {
        _.value.phone
      }
      prefWidth = 180
    }

    // Create table
    val table = new TableView[Person](model.getTeamMembers) {
      columns ++= Seq(firstNameColumn, lastNameColumn, phoneColumn)
    }

    // Listen to row selection, and print values of the selected row
    table.selectionModel().selectedItem.onChange(
      (_, _, newValue) => println(s"$newValue chosen in TableView")
    )

    table
  }
--#

--% Program.css
.table-row-cell {
  -fx-cell-size: 50px;
}
.table-view .table-cell{
  -fx-font-weight:bold;
  -fx-font-size:20px;
  /* -fx-text-fill:orange; */
}

#newButton {
  -fx-padding: 4 4 4 4;
}

#editButton {
  -fx-padding: 4 4 4 4;
}

#deleteButton {
  -fx-padding: 4 4 4 4;
}

#boldButton {
  -fx-padding: 4 4 4 4;
}

#italicButton {
  -fx-padding: 4 4 4 4;
}

#leftAlignButton {
  -fx-padding: 4 4 4 4;
}

#centerAlignButton {
  -fx-padding: 4 4 4 4;
}

#rightAlignButton {
  -fx-padding: 4 4 4 4;
}
--#

--% Model.scala
package be.fulgent.scalafx.model
import scalafx.beans.property.StringProperty

import scalafx.beans.property.DoubleProperty
import scalafx.collections.ObservableBuffer
import org.jsoup._
import collection.JavaConverters._

class StarterAppModel {

  val listViewItems = new ObservableBuffer[String]()
  val choiceBoxItems = ObservableBuffer("Choice A", "Choice B", "Choice C", "Choice D")
  val maxRpm: Double = 8000d
  val rpm = new DoubleProperty(this, "rpm", 0)
  val maxKph: Double = 300.0
  val kph = new DoubleProperty(this, "kph", 0)


  def getArticles: ObservableBuffer[Person] = {
    val alamat = "https://www.dailymail.co.uk/ushome/index.html"
    val doc = Jsoup.connect(alamat).get()
    val headlines = doc.select("div.article")
    // val judul = headlines.select("h2 a").text
    // val link = headlines.select("h2 a").href
    // val text = headlines.select("div.articletext p").text
    // for(headline <- headlines.asScala) yield (headline.attr("title"), headline.attr("href"))
    // for(headline <- headlines.asScala) yield headline.text

    val kembalian = new ObservableBuffer[Person]()

    for (headline <- headlines.asScala) {
      val judul = headline.select("h2 a").text
      val link = headline.select("h2 a").attr("href")
      val text = headline.select("div.articletext p").text
      // println(s"judul ${judul}, link ${link}, text ${text}")

      kembalian += new Person(judul, text, link)
    }

    kembalian
  }

  def getTeamMembers: ObservableBuffer[Person] = {

    getArticles

    // val teamMembers = new ObservableBuffer[Person]()

    // for (i <- 1 to 1000) {
    //   teamMembers += new Person("FirstName" + i, "LastName" + i, "Phone" + i)
    // }

    // teamMembers
  }


  def randomWebSite(): String = {

    val webSites: Array[String] = Array(
      "http://javafx.com",
      "http://fxexperience.com",
      "http://steveonjava.com",
      "http://javafxpert.com",
      "http://pleasingsoftware.blogspot.com",
      "http://www.weiqigao.com/blog",
      "http://google.com"
    )

    val randomIdx = (math.random * webSites.length).toInt
    webSites(randomIdx)
  }

}

class Person(firstName_ : String, lastName_ : String, phone_ : String) {

  val firstName = new StringProperty(this, "firstName", firstName_)
  val lastName = new StringProperty(this, "lastName", lastName_)
  val phone = new StringProperty(this, "phone", phone_)


  override def toString: String = {
    "Person: " + firstName() + " " + lastName()
  }
}
--#

--% Program.scala/main
package be.fulgent.scalafx.ui
import be.fulgent.scalafx.model.{StarterAppModel, Person}

import scalafx.Includes._
import scalafx.application.JFXApp
import scalafx.application.JFXApp.PrimaryStage
import scalafx.geometry.{Insets, Orientation, Pos}
import scalafx.scene.control.MenuItem._
import scalafx.scene.control.ScrollPane.ScrollBarPolicy
import scalafx.scene.control._
import scalafx.scene.image.{Image, ImageView}
import scalafx.scene.input.KeyCombination
import scalafx.scene.layout.{BorderPane, HBox, StackPane, VBox}
import scalafx.scene.paint.Color
import scalafx.scene.shape.{Circle, Rectangle}
import scalafx.scene.web.{HTMLEditor, WebView}
import scalafx.scene.{Node, Scene}
import scalafx.stage.Popup


object Program extends JFXApp {

  private val filecss = "Program.css"
  private val filepng = "images/paper.png"
  private val model = new StarterAppModel()

  stage = new PrimaryStage {
    scene = new Scene(1350, 750) {
      // ini butuh di build.sbt
      // resourceDirectory in Compile := baseDirectory(_ / "src").value
      // agar resource dicopy ke classes/
      stylesheets = List(getClass.getResource(filecss).toExternalForm)
      root = new BorderPane {
        top = new VBox {
          children = List(
            createMenus(),
            createToolBar()
          )
          center = createTabs()
        }
      }
    }
    title = "Aplikasi ScalaFX jaman now!"
  }


  private def createMenus() = new MenuBar {
    menus = List(
      new Menu("File") {
        items = List(
          new MenuItem("New...") {
            graphic = new ImageView(new Image(this, filepng))
            accelerator = KeyCombination.keyCombination("Ctrl +N")
            onAction = e => println(s"${e.eventType} occurred on MenuItem New")
          },
          new MenuItem("Save")
        )
      },
      new Menu("Edit") {
        items = List(
          new MenuItem("Cut"),
          new MenuItem("Copy"),
          new MenuItem("Paste")
        )
      }
    )
  }


  private def createToolBar(): ToolBar = {
    val alignToggleGroup = new ToggleGroup()
    val toolBar = new ToolBar {
      content = List(
        new Button {
          id = "newButton"
          graphic = new ImageView(new Image(this, filepng))
          tooltip = Tooltip("New Document... Ctrl+N")
          onAction = () => println("New toolbar button clicked")
        },
        new Button {
          id = "editButton"
          graphic = new Circle {
            fill = Color.Green
            radius = 8
          }
        },
        new Button {
          id = "deleteButton"
          graphic = new Circle {
            fill = Color.Blue
            radius = 8
          }
        },
        new Separator {
          orientation = Orientation.Vertical
        },
        new ToggleButton {
          id = "boldButton"
          graphic = new Circle {
            fill = Color.Maroon
            radius = 8
          }
          onAction = e => {
              val tb = e.getTarget.asInstanceOf[javafx.scene.control.ToggleButton]
            print(s"${e.eventType} occurred on ToggleButton ${tb.id}")
              print(", and selectedProperty is: ")
              println(tb.selectedProperty.value)
          }
        },
        new ToggleButton {
          id = "italicButton"
          graphic = new Circle {
            fill = Color.Yellow
            radius = 8
          }
          onAction = e => {
              val tb = e.getTarget.asInstanceOf[javafx.scene.control.ToggleButton]
            print(s"${e.eventType} occurred on ToggleButton ${tb.id}")
              print(", and selectedProperty is: ")
              println(tb.selectedProperty.value)
          }
        },
        new Separator {
          orientation = Orientation.Vertical
        },
        new ToggleButton {
          id = "leftAlignButton"
          toggleGroup = alignToggleGroup
          graphic = new Circle {
            fill = Color.Purple
            radius = 8
          }
        },
        new ToggleButton {
          toggleGroup = alignToggleGroup
          id = "centerAlignButton"
          graphic = new Circle {
            fill = Color.Orange
            radius = 8
          }
        },
        new ToggleButton {
          toggleGroup = alignToggleGroup
          id = "rightAlignButton"
          graphic = new Circle {
            fill = Color.Cyan
            radius = 8
          }
        }
      )
    }

    alignToggleGroup.selectToggle(alignToggleGroup.toggles(0))
    alignToggleGroup.selectedToggle.onChange {
      val tb = alignToggleGroup.selectedToggle.get.asInstanceOf[javafx.scene.control.ToggleButton]
      println(tb.id() + " selected")
    }

    toolBar
  }


  private def createTabs(): TabPane = {
    new TabPane {
      tabs = List(
        new Tab {
          text = "TableView"
          content = createTableDemoNode()
          closable = false
        },
        // new Tab {
        //   text = "Accordion/TitledPane"
        //   content = createAccordionTitledDemoNode()
        //   closable = false
        // },
        // new Tab {
        //   text = "SplitPane/TreeView/ListView"
        //   content = createSplitTreeListDemoNode()
        //   closable = false
        // },
        // new Tab {
        //   text = "ScrollPane/Miscellaneous"
        //   content = createScrollMiscDemoNode()
        //   closable = false
        // },
        // new Tab {
        //   text = "HTMLEditor"
        //   content = createHtmlEditorDemoNode()
        //   closable = false
        // },
        // new Tab {
        //   // Name a reference to itself
        //   inner =>
        //   val webView = new WebView()
        //   text = "WebView"
        //   content = webView
        //   closable = false
        //   onSelectionChanged = () => {
        //     val randomWebSite = model.randomWebSite()
        //     if (inner.selected()) {
        //       webView.engine.load(randomWebSite)
        //       println("WebView tab is selected, loading: " + randomWebSite)
        //     }
        //     println("")
        //   }
        // }
      )
    }
  }


  private def createTableDemoNode(): Node = {
    // Create columns
    val firstNameColumn = new TableColumn[Person, String] {
      text = "First Name"
      cellValueFactory = {
        _.value.firstName
      }
      prefWidth = 1080
    }
    val lastNameColumn = new TableColumn[Person, String] {
      text = "Last Name"
      cellValueFactory = {
        _.value.lastName
      }
      prefWidth = 180
    }
    val phoneColumn = new TableColumn[Person, String] {
      text = "Phone"
      cellValueFactory = {
        _.value.phone
      }
      prefWidth = 180
    }

    // Create table
    val table = new TableView[Person](model.getTeamMembers) {
      columns ++= Seq(firstNameColumn, lastNameColumn, phoneColumn)
    }

    // Listen to row selection, and print values of the selected row
    table.selectionModel().selectedItem.onChange(
      (_, _, newValue) => println(s"$newValue chosen in TableView")
    )

    table
  }


  private def createAccordionTitledDemoNode(): Node = new Accordion {
    panes = List(
      new TitledPane() {
        text = "TitledPane A"
        content = new TextArea {
          text = "TitledPane A content"
        }
      },
      new TitledPane {
        text = "TitledPane B"
        content = new TextArea {
          text = "TitledPane B content"
        }
      },
      new TitledPane {
        text = "TitledPane C"
        content = new TextArea {
          text = "TitledPane C' content"
        }
      }
    )

    expandedPane = panes.head
  }


  private def createSplitTreeListDemoNode(): Node = {
    val treeView = new TreeView[String] {
      minWidth = 150
      showRoot = false
      editable = false
      root = new TreeItem[String] {
        value = "Root"
        children = List(
          new TreeItem("Animal") {
            children = List(
              new TreeItem("Lion"),
              new TreeItem("Tiger"),
              new TreeItem("Bear")
            )
          },
          new TreeItem("Mineral") {
            children = List(
              new TreeItem("Copper"),
              new TreeItem("Diamond"),
              new TreeItem("Quartz")
            )
          },
          new TreeItem("Vegetable") {
            children = List(
              new TreeItem("Arugula"),
              new TreeItem("Broccoli"),
              new TreeItem("Cabbage")
            )
          }
        )
      }
    }

    val listView = new ListView[String] {
      items = model.listViewItems
    }

    treeView.selectionModel().selectionMode = SelectionMode.Single
    treeView.selectionModel().selectedItem.onChange(
      (_, _, newTreeItem) => {
        if (newTreeItem != null && newTreeItem.isLeaf) {
          model.listViewItems.clear()
          for (i <- 1 to 10000) {
            model.listViewItems += newTreeItem.getValue + " " + i
          }
        }
      }
    )

    new SplitPane {
      items ++= List(
        treeView,
        listView
      )
    }
  }


  private def createScrollMiscDemoNode(): Node = {
    val radioToggleGroup = new ToggleGroup()
    val variousControls = new VBox {
      padding = Insets(10)
      spacing = 20
      children = List(
        new Button("Button") {
          onAction = e => println(s"${e.eventType} occurred on Button")
        },
        new CheckBox("CheckBox") {
          inner =>
          onAction = e =>
            println(s"${e.eventType} occurred on CheckBox, and `selected` property is: ${inner.selected()}")
        },
        new HBox {
          spacing = 10
          children = List(
            new RadioButton("RadioButton1") {
              toggleGroup = radioToggleGroup
            },
            new RadioButton("RadioButton2") {
              toggleGroup = radioToggleGroup
            }
          )
        },
        new Hyperlink("Hyperlink") {
          onAction = e => println(s"${e.eventType} occurred on Hyperlink")
        },
        new ChoiceBox(model.choiceBoxItems) {
          selectionModel().selectFirst()
          selectionModel().selectedItem.onChange(
            (_, _, newValue) => println(s"$newValue chosen in ChoiceBox")
          )
        },
        new MenuButton("MenuButton") {
          items = List(
            new MenuItem("MenuItem A") {
              onAction = ae => println(s"${ae.eventType} occurred on Menu Item A")
            },
            new MenuItem("MenuItem B")
          )
        },
        new SplitMenuButton {
          text = "SplitMenuButton"
          onAction = ae => println(s"${ae.eventType} occurred on SplitMenuButton")
          items = List(
            new MenuItem("MenuItem A") {
              onAction = ae => println(s"${ae.eventType} occurred on Menu Item A")
            },
            new MenuItem("MenuItem B")
          )
        },
        new TextField {
          promptText = "Enter user name"
          prefColumnCount = 16
          text.onChange {
            println("TextField text is: " + text())
          }
        },
        new PasswordField {
          promptText = "Enter password"
          prefColumnCount = 16
          text.onChange {
            println("PasswordField text is: " + text())
          }
        },
        new HBox {
          spacing = 10
          children = List(
            new Label {
              text = "TextArea"
            },
            new TextArea {
              prefColumnCount = 12
              prefRowCount = 4
              text.onChange {
                println("TextArea text is: " + text())
              }
            }
          )
        },
        new ProgressIndicator {
          prefWidth = 200
          progress <== model.rpm / model.maxRpm
        },
        new Slider {
          prefWidth = 200
          min = -1
          max = model.maxRpm
          value <==> model.rpm
        },
        new ProgressBar {
          prefWidth = 200
          progress <== model.kph / model.maxKph
        },
        new ScrollBar {
          prefWidth = 200
          min = -1
          max = model.maxKph
          value <==> model.kph
        }
      )
    }

    radioToggleGroup.selectToggle(radioToggleGroup.toggles(0))
    radioToggleGroup.selectedToggle.onChange {
      val rb = radioToggleGroup.selectedToggle.get.asInstanceOf[javafx.scene.control.ToggleButton]
      if (rb != null) println(rb.id() + " selected")
    }

    val sampleContextMenu = new ContextMenu {
      items ++= Seq(
        new MenuItem("MenuItemA") {
          onAction = e => println(s"${e.eventType} occurred on Menu Item A")
        },
        new MenuItem("MenuItemB") {
          onAction = e => println(s"${e.eventType} occurred on Menu Item B")
        })
    }

    new ScrollPane {
      content = variousControls
      hbarPolicy = ScrollBarPolicy.Always
      vbarPolicy = ScrollBarPolicy.AsNeeded
      contextMenu = sampleContextMenu
    }
  }


  private def createHtmlEditorDemoNode(): Node = {

    val htmlEditor = new HTMLEditor {
      htmlText = "<p>Replace this text</p>"
    }

    val viewHTMLButton = new Button("View HTML") {
      onAction = () => {
        val alertPopup = createAlertPopup(htmlEditor.htmlText)
        alertPopup.show(stage,
          (stage.width() - alertPopup.width()) / 2.0 + stage.x(),
          (stage.height() - alertPopup.height()) / 2.0 + stage.y())
      }
      alignmentInParent = Pos.Center
      margin = Insets(10, 0, 10, 0)
    }

    new BorderPane {
      center = htmlEditor
      bottom = viewHTMLButton
    }
  }


  private def createAlertPopup(popupText: String) = new Popup {
    inner =>
    content.add(new StackPane {
      children = List(
        new Rectangle {
          width = 300
          height = 200
          arcWidth = 20
          arcHeight = 20
          fill = Color.LightBlue
          stroke = Color.Gray
          strokeWidth = 2
        },
        new BorderPane {
          center = new Label {
            text = popupText
            wrapText = true
            maxWidth = 280
            maxHeight = 140
          }
          bottom = new Button("OK") {
            onAction = () => inner.hide()
            alignmentInParent = Pos.Center
            margin = Insets(10, 0, 10, 0)
          }
        }
      )
    }.delegate
    )
  }

}
--#


--% build.sbt
name := "myscalafxproj"
organization := "fulgent"
version := "0.1-SNAPSHOT"
scalaVersion := "2.13.1"

// Set the main Scala source directory to be <base>/src
// scalaSource in Compile := baseDirectory(_ / "src").value

resourceDirectory in Compile := baseDirectory(_ / "src").value

// Append -deprecation to the options passed to the Scala compiler
// scalacOptions ++= Seq("-deprecation", "-feature")

// Point to location of a snapshot repository for ScalaFX
// resolvers += Opts.resolver.sonatypeSnapshots

libraryDependencies ++= Seq(
  "org.scalafx"   %% "scalafx"   % "14-R19",
  "org.scalatest" %% "scalatest" % "3.1.2" % "test" //http://www.scalatest.org/download
)

// Determine OS version of JavaFX binaries
lazy val osName = System.getProperty("os.name") match {
  case n if n.startsWith("Linux") => "linux"
  case n if n.startsWith("Mac") => "mac"
  case n if n.startsWith("Windows") => "win"
  case _ => throw new Exception("Unknown platform!")
}

// Add JavaFX dependencies
lazy val javaFXModules = Seq("base", "controls", "fxml", "graphics", "media", "swing", "web")
libraryDependencies ++= javaFXModules.map( m=>
  "org.openjfx" % s"javafx-$m" % "14.0.1" classifier osName
)
// https://mvnrepository.com/artifact/org.jsoup/jsoup
libraryDependencies += "org.jsoup" % "jsoup" % "1.13.1"


// Fork a new JVM for 'run' and 'test:run' to avoid JavaFX double initialization problems
fork := true

// set the main class for the main 'run' task
// change Compile to Test to set it for 'test:run'
//mainClass in (Compile, run) := Some("my.scalafx.ScalaFXHelloWorld")
mainClass in (Compile, run) := Some("be.fulgent.scalafx.ui.Program")

shellPrompt := { _ => System.getProperty("user.name") + "> " }
--#

--% Program.scala/unworthy/update
package be.fulgent.scalafx.ui
import be.fulgent.scalafx.model.{Person, StarterAppModel}

import scalafx.Includes._
import scalafx.application.JFXApp
import scalafx.application.JFXApp.PrimaryStage
import scalafx.geometry.{Insets, Orientation, Pos}
import scalafx.scene.control.MenuItem._
import scalafx.scene.control.ScrollPane.ScrollBarPolicy
import scalafx.scene.control._
import scalafx.scene.image.{Image, ImageView}
import scalafx.scene.input.KeyCombination
import scalafx.scene.layout.{BorderPane, HBox, StackPane, VBox}
import scalafx.scene.paint.Color
import scalafx.scene.shape.{Circle, Rectangle}
import scalafx.scene.web.{HTMLEditor, WebView}
import scalafx.scene.{Node, Scene}
import scalafx.stage.Popup
import javafx.application.Application
import javafx.application.Application.Parameters

object Program extends JFXApp {

  private val filecss = "Program.css"
  private val filepng = "images/paper.png"
  private val model = new StarterAppModel()

  // https://stackoverflow.com/questions/10134856/javafx-2-0-how-to-application-getparameters-in-a-controller-java-file
  // public static String parameters;
  // parameters = getParameters().getNamed().toString();
  
  // private val parameters: Parameters = Application.getParameters()
  // println("Iterasi parameters:")
  // parameters.getRaw().forEach(println)

  stage = new PrimaryStage {
    scene = new Scene(1350, 768) {
      // ini butuh di build.sbt
      // resourceDirectory in Compile := baseDirectory(_ / "src").value
      // agar resource dicopy ke classes/
      stylesheets = List(getClass.getResource(filecss).toExternalForm)

      root = new BorderPane {
        top = new VBox {
          children = List(
            createMenus(),
            createToolBar()
          )
          center = createTabs()
        }
      }

    }
    title = "Aplikasi ScalaFX jaman now!"
  }


  private def createMenus() = new MenuBar {
    menus = List(
      new Menu("File") {
        items = List(
          new MenuItem("New...") {
            graphic = new ImageView(new Image(this, filepng))
            accelerator = KeyCombination.keyCombination("Ctrl +N")
            onAction = e => println(s"${e.eventType} occurred on MenuItem New")
          },
          new MenuItem("Save")
        )
      },
      new Menu("Edit") {
        items = List(
          new MenuItem("Cut"),
          new MenuItem("Copy"),
          new MenuItem("Paste")
        )
      }
    )
  }


  private def createToolBar(): ToolBar = {
    val alignToggleGroup = new ToggleGroup()
    val toolBar = new ToolBar {
      content = List(
        new Button {
          id = "newButton"
          graphic = new ImageView(new Image(this, filepng))
          tooltip = Tooltip("New Document... Ctrl+N")
          onAction = () => println("New toolbar button clicked")
        },
        new Button {
          id = "editButton"
          graphic = new Circle {
            fill = Color.Green
            radius = 8
          }
        },
        new Button {
          id = "deleteButton"
          graphic = new Circle {
            fill = Color.Blue
            radius = 8
          }
        },
        new Separator {
          orientation = Orientation.Vertical
        },
        new ToggleButton {
          id = "boldButton"
          graphic = new Circle {
            fill = Color.Maroon
            radius = 8
          }
          onAction = e => {
              val tb = e.getTarget.asInstanceOf[javafx.scene.control.ToggleButton]
            print(s"${e.eventType} occurred on ToggleButton ${tb.id}")
              print(", and selectedProperty is: ")
              println(tb.selectedProperty.value)
          }
        },
        new ToggleButton {
          id = "italicButton"
          graphic = new Circle {
            fill = Color.Yellow
            radius = 8
          }
          onAction = e => {
              val tb = e.getTarget.asInstanceOf[javafx.scene.control.ToggleButton]
            print(s"${e.eventType} occurred on ToggleButton ${tb.id}")
              print(", and selectedProperty is: ")
              println(tb.selectedProperty.value)
          }
        },
        new Separator {
          orientation = Orientation.Vertical
        },
        new ToggleButton {
          id = "leftAlignButton"
          toggleGroup = alignToggleGroup
          graphic = new Circle {
            fill = Color.Purple
            radius = 8
          }
        },
        new ToggleButton {
          toggleGroup = alignToggleGroup
          id = "centerAlignButton"
          graphic = new Circle {
            fill = Color.Orange
            radius = 8
          }
        },
        new ToggleButton {
          toggleGroup = alignToggleGroup
          id = "rightAlignButton"
          graphic = new Circle {
            fill = Color.Cyan
            radius = 8
          }
        }
      )
    }

    alignToggleGroup.selectToggle(alignToggleGroup.toggles(0))
    alignToggleGroup.selectedToggle.onChange {
      val tb = alignToggleGroup.selectedToggle.get.asInstanceOf[javafx.scene.control.ToggleButton]
      println(tb.id() + " selected")
    }

    toolBar
  }


  private def createTabs(): TabPane = {
    new TabPane {
      tabs = List(
        new Tab {
          text = "TableView"
          content = createTableDemoNode()
          closable = false
        },
        // new Tab {
        //   text = "Accordion/TitledPane"
        //   content = createAccordionTitledDemoNode()
        //   closable = false
        // },
        // new Tab {
        //   text = "SplitPane/TreeView/ListView"
        //   content = createSplitTreeListDemoNode()
        //   closable = false
        // },
        // new Tab {
        //   text = "ScrollPane/Miscellaneous"
        //   content = createScrollMiscDemoNode()
        //   closable = false
        // },
        // new Tab {
        //   text = "HTMLEditor"
        //   content = createHtmlEditorDemoNode()
        //   closable = false
        // },
        // new Tab {
        //   // Name a reference to itself
        //   inner =>
        //   val webView = new WebView()
        //   text = "WebView"
        //   content = webView
        //   closable = false
        //   onSelectionChanged = () => {
        //     val randomWebSite = model.randomWebSite()
        //     if (inner.selected()) {
        //       webView.engine.load(randomWebSite)
        //       println("WebView tab is selected, loading: " + randomWebSite)
        //     }
        //     println("")
        //   }
        // }
      )
    }
  }


  private def createTableDemoNode(): Node = {
    // Create columns
    val firstNameColumn = new TableColumn[Person, String] {
      text = "First Name"
      cellValueFactory = {
        _.value.firstName
      }
      prefWidth = 800
    }
    val lastNameColumn = new TableColumn[Person, String] {
      text = "Last Name"
      cellValueFactory = {
        _.value.lastName
      }
      prefWidth = 180
    }
    val phoneColumn = new TableColumn[Person, String] {
      text = "Phone"
      cellValueFactory = {
        _.value.phone
      }
      prefWidth = 180
    }

    // Create table
    val table = new TableView[Person](model.getTeamMembers) {
      columns ++= Seq(firstNameColumn, lastNameColumn, phoneColumn)
    }

    // Listen to row selection, and print values of the selected row
    table.selectionModel().selectedItem.onChange(
      (_, _, newValue) => println(s"$newValue chosen in TableView")
    )

    table
  }


  private def createAccordionTitledDemoNode(): Node = new Accordion {
    panes = List(
      new TitledPane() {
        text = "TitledPane A"
        content = new TextArea {
          text = "TitledPane A content"
        }
      },
      new TitledPane {
        text = "TitledPane B"
        content = new TextArea {
          text = "TitledPane B content"
        }
      },
      new TitledPane {
        text = "TitledPane C"
        content = new TextArea {
          text = "TitledPane C' content"
        }
      }
    )

    expandedPane = panes.head
  }


  private def createSplitTreeListDemoNode(): Node = {
    val treeView = new TreeView[String] {
      minWidth = 150
      showRoot = false
      editable = false
      root = new TreeItem[String] {
        value = "Root"
        children = List(
          new TreeItem("Animal") {
            children = List(
              new TreeItem("Lion"),
              new TreeItem("Tiger"),
              new TreeItem("Bear")
            )
          },
          new TreeItem("Mineral") {
            children = List(
              new TreeItem("Copper"),
              new TreeItem("Diamond"),
              new TreeItem("Quartz")
            )
          },
          new TreeItem("Vegetable") {
            children = List(
              new TreeItem("Arugula"),
              new TreeItem("Broccoli"),
              new TreeItem("Cabbage")
            )
          }
        )
      }
    }

    val listView = new ListView[String] {
      items = model.listViewItems
    }

    treeView.selectionModel().selectionMode = SelectionMode.Single
    treeView.selectionModel().selectedItem.onChange(
      (_, _, newTreeItem) => {
        if (newTreeItem != null && newTreeItem.isLeaf) {
          model.listViewItems.clear()
          for (i <- 1 to 10000) {
            model.listViewItems += newTreeItem.getValue + " " + i
          }
        }
      }
    )

    new SplitPane {
      items ++= List(
        treeView,
        listView
      )
    }
  }


  private def createScrollMiscDemoNode(): Node = {
    val radioToggleGroup = new ToggleGroup()
    val variousControls = new VBox {
      padding = Insets(10)
      spacing = 20
      children = List(
        new Button("Button") {
          onAction = e => println(s"${e.eventType} occurred on Button")
        },
        new CheckBox("CheckBox") {
          inner =>
          onAction = e =>
            println(s"${e.eventType} occurred on CheckBox, and `selected` property is: ${inner.selected()}")
        },
        new HBox {
          spacing = 10
          children = List(
            new RadioButton("RadioButton1") {
              toggleGroup = radioToggleGroup
            },
            new RadioButton("RadioButton2") {
              toggleGroup = radioToggleGroup
            }
          )
        },
        new Hyperlink("Hyperlink") {
          onAction = e => println(s"${e.eventType} occurred on Hyperlink")
        },
        new ChoiceBox(model.choiceBoxItems) {
          selectionModel().selectFirst()
          selectionModel().selectedItem.onChange(
            (_, _, newValue) => println(s"$newValue chosen in ChoiceBox")
          )
        },
        new MenuButton("MenuButton") {
          items = List(
            new MenuItem("MenuItem A") {
              onAction = ae => println(s"${ae.eventType} occurred on Menu Item A")
            },
            new MenuItem("MenuItem B")
          )
        },
        new SplitMenuButton {
          text = "SplitMenuButton"
          onAction = ae => println(s"${ae.eventType} occurred on SplitMenuButton")
          items = List(
            new MenuItem("MenuItem A") {
              onAction = ae => println(s"${ae.eventType} occurred on Menu Item A")
            },
            new MenuItem("MenuItem B")
          )
        },
        new TextField {
          promptText = "Enter user name"
          prefColumnCount = 16
          text.onChange {
            println("TextField text is: " + text())
          }
        },
        new PasswordField {
          promptText = "Enter password"
          prefColumnCount = 16
          text.onChange {
            println("PasswordField text is: " + text())
          }
        },
        new HBox {
          spacing = 10
          children = List(
            new Label {
              text = "TextArea"
            },
            new TextArea {
              prefColumnCount = 12
              prefRowCount = 4
              text.onChange {
                println("TextArea text is: " + text())
              }
            }
          )
        },
        new ProgressIndicator {
          prefWidth = 200
          progress <== model.rpm / model.maxRpm
        },
        new Slider {
          prefWidth = 200
          min = -1
          max = model.maxRpm
          value <==> model.rpm
        },
        new ProgressBar {
          prefWidth = 200
          progress <== model.kph / model.maxKph
        },
        new ScrollBar {
          prefWidth = 200
          min = -1
          max = model.maxKph
          value <==> model.kph
        }
      )
    }

    radioToggleGroup.selectToggle(radioToggleGroup.toggles(0))
    radioToggleGroup.selectedToggle.onChange {
      val rb = radioToggleGroup.selectedToggle.get.asInstanceOf[javafx.scene.control.ToggleButton]
      if (rb != null) println(rb.id() + " selected")
    }

    val sampleContextMenu = new ContextMenu {
      items ++= Seq(
        new MenuItem("MenuItemA") {
          onAction = e => println(s"${e.eventType} occurred on Menu Item A")
        },
        new MenuItem("MenuItemB") {
          onAction = e => println(s"${e.eventType} occurred on Menu Item B")
        })
    }

    new ScrollPane {
      content = variousControls
      hbarPolicy = ScrollBarPolicy.Always
      vbarPolicy = ScrollBarPolicy.AsNeeded
      contextMenu = sampleContextMenu
    }
  }


  private def createHtmlEditorDemoNode(): Node = {

    val htmlEditor = new HTMLEditor {
      htmlText = "<p>Replace this text</p>"
    }

    val viewHTMLButton = new Button("View HTML") {
      onAction = () => {
        val alertPopup = createAlertPopup(htmlEditor.htmlText)
        alertPopup.show(stage,
          (stage.width() - alertPopup.width()) / 2.0 + stage.x(),
          (stage.height() - alertPopup.height()) / 2.0 + stage.y())
      }
      alignmentInParent = Pos.Center
      margin = Insets(10, 0, 10, 0)
    }

    new BorderPane {
      center = htmlEditor
      bottom = viewHTMLButton
    }
  }


  private def createAlertPopup(popupText: String) = new Popup {
    inner =>
    content.add(new StackPane {
      children = List(
        new Rectangle {
          width = 300
          height = 200
          arcWidth = 20
          arcHeight = 20
          fill = Color.LightBlue
          stroke = Color.Gray
          strokeWidth = 2
        },
        new BorderPane {
          center = new Label {
            text = popupText
            wrapText = true
            maxWidth = 280
            maxHeight = 140
          }
          bottom = new Button("OK") {
            onAction = () => inner.hide()
            alignmentInParent = Pos.Center
            margin = Insets(10, 0, 10, 0)
          }
        }
      )
    }.delegate
    )
  }
}
--#
