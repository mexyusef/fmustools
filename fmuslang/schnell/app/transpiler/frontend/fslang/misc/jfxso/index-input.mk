--% index/fmus
jfxso,d(/mk)
	%utama=__FILE__
	build.gradle,f(e=utama=C:/work/oprek/coba/stackoverflow/javaso/build.gradle)
	.gradle,d(/mk)
		file-system.probe,f(b64=utama=C:/work/oprek/coba/stackoverflow/javaso/.gradle/file-system.probe)
		7.3,d(/mk)
			gc.properties,f(e=utama=C:/work/oprek/coba/stackoverflow/javaso/.gradle/7.3/gc.properties)
			checksums,d(/mk)
				checksums.lock,f(b64=utama=C:/work/oprek/coba/stackoverflow/javaso/.gradle/7.3/checksums/checksums.lock)
			dependencies-accessors,d(/mk)
				dependencies-accessors.lock,f(b64=utama=C:/work/oprek/coba/stackoverflow/javaso/.gradle/7.3/dependencies-accessors/dependencies-accessors.lock)
				gc.properties,f(e=utama=C:/work/oprek/coba/stackoverflow/javaso/.gradle/7.3/dependencies-accessors/gc.properties)
			fileChanges,d(/mk)
			fileHashes,d(/mk)
				fileHashes.lock,f(b64=utama=C:/work/oprek/coba/stackoverflow/javaso/.gradle/7.3/fileHashes/fileHashes.lock)
			vcsMetadata,d(/mk)
		7.3.3,d(/mk)
			gc.properties,f(e=utama=C:/work/oprek/coba/stackoverflow/javaso/.gradle/7.3.3/gc.properties)
			checksums,d(/mk)
				checksums.lock,f(b64=utama=C:/work/oprek/coba/stackoverflow/javaso/.gradle/7.3.3/checksums/checksums.lock)
			dependencies-accessors,d(/mk)
				dependencies-accessors.lock,f(b64=utama=C:/work/oprek/coba/stackoverflow/javaso/.gradle/7.3.3/dependencies-accessors/dependencies-accessors.lock)
				gc.properties,f(e=utama=C:/work/oprek/coba/stackoverflow/javaso/.gradle/7.3.3/dependencies-accessors/gc.properties)
			executionHistory,d(/mk)
				executionHistory.lock,f(b64=utama=C:/work/oprek/coba/stackoverflow/javaso/.gradle/7.3.3/executionHistory/executionHistory.lock)
			fileChanges,d(/mk)
			fileHashes,d(/mk)
				fileHashes.lock,f(b64=utama=C:/work/oprek/coba/stackoverflow/javaso/.gradle/7.3.3/fileHashes/fileHashes.lock)
			vcsMetadata,d(/mk)
		buildOutputCleanup,d(/mk)
			buildOutputCleanup.lock,f(b64=utama=C:/work/oprek/coba/stackoverflow/javaso/.gradle/buildOutputCleanup/buildOutputCleanup.lock)
			cache.properties,f(e=utama=C:/work/oprek/coba/stackoverflow/javaso/.gradle/buildOutputCleanup/cache.properties)
		vcs-1,d(/mk)
			gc.properties,f(e=utama=C:/work/oprek/coba/stackoverflow/javaso/.gradle/vcs-1/gc.properties)
	src,d(/mk)
		main,d(/mk)
			java,d(/mk)
				be,d(/mk)
					fulgent,d(/mk)
						fxapp,d(/mk)
							Question.java,f(e=utama=C:/work/oprek/coba/stackoverflow/javaso/src/main/java/be/fulgent/fxapp/Question.java)
							Startup.java,f(e=utama=C:/work/oprek/coba/stackoverflow/javaso/src/main/java/be/fulgent/fxapp/Startup.java)
			resources,d(/mk)
				gaya.css,f(e=utama=C:/work/oprek/coba/stackoverflow/javaso/src/main/resources/gaya.css)
	$*cmd.exe /c start cmd.exe /k "gradle run"
--#

--% C:/work/oprek/coba/stackoverflow/javaso/build.gradle
plugins {
	id 'java'
	id 'application'
	id 'org.openjfx.javafxplugin' version '0.0.9'
}

group 'be.fulgent'
version '1.0-SNAPSHOT'

repositories {
	mavenCentral()
	jcenter()
}

dependencies {
	// testCompile group: 'junit', name: 'junit', version: '4.12'

	implementation 'com.google.guava:guava:29.0-jre'
	implementation 'org.glassfish:javax.json:1.1'
	implementation 'com.gluonhq:connect:1.4.3'
	implementation "jakarta.xml.bind:jakarta.xml.bind-api:2.3.2"
	implementation "org.glassfish.jaxb:jaxb-runtime:2.3.2"
	implementation 'org.json:json:20201115'
	implementation 'org.jsoup:jsoup:1.13.1'
}


def packagename = 'be.fulgent.fxapp'
// ternyata . di-esc bukan \. tapi \\.
def packagefolder = packagename.replaceAll('\\.','/')

application {
	// mainClassName = "${packagename}.Program"
	mainClassName = "${packagename}.Startup"
}

javafx {
	modules = [ 'javafx.controls', 'javafx.fxml', 'javafx.graphics', 'javafx.web' ]
}

//sourceSets {
// 	main {
//	//output.resourcesDir = "$buildDir/classes/java/$name/${packagename}"
//	//output.resourcesDir = "build/classes/java/$name/$packagename"
//	//output.resourcesDir = "build/classes/java/$name/${packagename.replaceAll('.','/')}"
//	output.resourcesDir = "build/classes/java/$name/$packagefolder"
//	}
//}

--#

--% C:/work/oprek/coba/stackoverflow/javaso/.gradle/file-system.probe
AAABftdRjS0=
--#

--% C:/work/oprek/coba/stackoverflow/javaso/.gradle/7.3/gc.properties

--#

--% C:/work/oprek/coba/stackoverflow/javaso/.gradle/7.3/checksums/checksums.lock
A/XJQg8KZeOYAAAAAAAAAAA=
--#

--% C:/work/oprek/coba/stackoverflow/javaso/.gradle/7.3/dependencies-accessors/dependencies-accessors.lock
A0h78ZnFGWJPAAAAAAAAAAA=
--#

--% C:/work/oprek/coba/stackoverflow/javaso/.gradle/7.3/dependencies-accessors/gc.properties

--#

--% C:/work/oprek/coba/stackoverflow/javaso/.gradle/7.3/fileHashes/fileHashes.lock
A5mnHKSpHYuZAAAAAAAAAAA=
--#

--% C:/work/oprek/coba/stackoverflow/javaso/.gradle/7.3.3/gc.properties

--#

--% C:/work/oprek/coba/stackoverflow/javaso/.gradle/7.3.3/checksums/checksums.lock
A5cXOyxYtUWaAAAAAAAAALU=
--#

--% C:/work/oprek/coba/stackoverflow/javaso/.gradle/7.3.3/dependencies-accessors/dependencies-accessors.lock
A+be8vvMVAi8AAAAAAAAAAA=
--#

--% C:/work/oprek/coba/stackoverflow/javaso/.gradle/7.3.3/dependencies-accessors/gc.properties

--#

--% C:/work/oprek/coba/stackoverflow/javaso/.gradle/7.3.3/executionHistory/executionHistory.lock
A/VhJlZAJX6SAAAAAAAAAAQ=
--#

--% C:/work/oprek/coba/stackoverflow/javaso/.gradle/7.3.3/fileHashes/fileHashes.lock
Azhzc4x3uf15AAAAAAAAAA8=
--#

--% C:/work/oprek/coba/stackoverflow/javaso/.gradle/buildOutputCleanup/buildOutputCleanup.lock
A5hEdcLXpH7KAAAAAAAAABo=
--#

--% C:/work/oprek/coba/stackoverflow/javaso/.gradle/buildOutputCleanup/cache.properties
#Tue Feb 08 10:11:06 ICT 2022
gradle.version=7.3.3

--#

--% C:/work/oprek/coba/stackoverflow/javaso/.gradle/vcs-1/gc.properties

--#

--% C:/work/oprek/coba/stackoverflow/javaso/src/main/java/be/fulgent/fxapp/Question.java
package be.fulgent.fxapp;

import java.text.SimpleDateFormat;
import java.util.Date;
import javafx.beans.property.SimpleStringProperty;
import javafx.beans.property.StringProperty;
import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;

@XmlAccessorType(XmlAccessType.PROPERTY)
public class Question {

	static final SimpleDateFormat sdf = new SimpleDateFormat ("dd-MM-YY");
	private StringProperty ownerProperty = new SimpleStringProperty();
	private String question;
	private String waktos;
	private String alamat;
	private String tags;


	public String getAlamat() {
		return alamat;
	}

	public void setAlamat(String alamat) {
		this.alamat = alamat;
	}

	public String getTags() {
		return tags;
	}

	public void setTags(String tags) {
		this.tags = tags;
	}

	public Question (String o, String q, String w, String a, String t) {
		this.ownerProperty.set(o);
		this.question = q;
		this.waktos = w;
		this.alamat = a;
		this.tags = t;
	}

	public String getOwner() {
		return ownerProperty.get();
	}

	public void setOwner(String owner) {
		this.ownerProperty.set(owner);
	}

	public String getQuestion() {
		return question;
	}

	public void setQuestion(String question) {
		this.question = question;
	}

	public String getWaktos() {
		return waktos;
	}

	public void setWaktos(String waktos) {
		this.waktos = waktos;
	}
}

--#

--% C:/work/oprek/coba/stackoverflow/javaso/src/main/java/be/fulgent/fxapp/Startup.java
package be.fulgent.fxapp;

import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;
import javafx.application.Application;
import static javafx.application.Application.launch;

import javafx.application.Platform;
import javafx.beans.InvalidationListener;
import javafx.beans.Observable;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.concurrent.Service;
import javafx.concurrent.Worker;
import javafx.event.ActionEvent;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.scene.Scene;
import javafx.geometry.Rectangle2D;
import javafx.scene.control.*;
import javafx.scene.input.*;
import javafx.scene.layout.BorderPane;
import javafx.stage.Screen;

import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;
import javafx.util.Callback;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.Reader;
import java.nio.charset.Charset;

import java.net.URL;
import java.net.URLConnection;
import java.net.MalformedURLException;
import java.util.List;
import java.util.concurrent.*;
import java.util.stream.Collectors;
import java.util.zip.GZIPInputStream;
//import javafx.collections.FXCollections;
//import javafx.collections.ObservableList;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import javafx.scene.web.WebView;


public class Startup extends Application {

	static final SimpleDateFormat sdf = new SimpleDateFormat("dd-MM-YY");
	static final String soUrl = "http://api.stackexchange.com/2.2/search?order=desc&sort=activity&tagged=javafx&site=stackoverflow";
	final String stackOverflow = "https://stackoverflow.com/questions";
	final int Pages = 5;
	double lebar, tinggi;
	int delayDetik = 5, periodeDetik = 60;
	final Clipboard clipboard = Clipboard.getSystemClipboard();
	TableView<Question> tableView = new TableView<>();
	ScheduledExecutorService scheduledExecutorService = Executors.newScheduledThreadPool(5);

	public static void main(String[] args) {
		launch(args);
	}

	public void copyClipboard(String nilai) {
		ClipboardContent content = new ClipboardContent();
//	content.putString("Some text");
//	content.putHtml("<b>Some</b> text");
		content.putString(nilai);
		clipboard.setContent(content);
	}

	public void scheduleWork() throws IOException {
		ScheduledFuture scheduledFuture = scheduledExecutorService
			.scheduleAtFixedRate(new Runnable() {
				@Override
				public void run() {
					//	System.out.println("Executed!");
					try {
						tableView.setItems(getObservableList());
					} catch (IOException e) {
						e.printStackTrace();
					}
				}
			},
		delayDetik, periodeDetik, TimeUnit.SECONDS);
	}

	@Override
	public void start(Stage primaryStage) throws Exception {

		tableView.setItems(getObservableList());
//	tableView.setItems(getObservableList2());


		TableColumn<Question, String> dateColumn = new TableColumn<>("Date");
		TableColumn<Question, String> ownerColumn = new TableColumn<>("Owner");
		TableColumn<Question, String> questionColumn = new TableColumn<>("Question");

		TableColumn<Question, String> tagsColumn = new TableColumn<>("Tags");
		TableColumn<Question, String> linkColumn = new TableColumn<>("Url");

//	dateColumn.setCellValueFactory(new PropertyValueFactory<>("timestampString"));
		dateColumn.setCellValueFactory(new PropertyValueFactory<>("waktos"));
		ownerColumn.setCellValueFactory(new PropertyValueFactory<>("owner"));
		questionColumn.setCellValueFactory(new PropertyValueFactory<>("question"));

		tagsColumn.setCellValueFactory(new PropertyValueFactory<>("tags"));
		linkColumn.setCellValueFactory(new PropertyValueFactory<>("alamat"));

		questionColumn.setPrefWidth(800);
		tableView.getColumns().addAll(questionColumn, tagsColumn, dateColumn, ownerColumn, linkColumn);

		tableView.setRowFactory(tv -> {
				final TableRow<Question> row = new TableRow<>();
//            row.hoverProperty().addListener(observable -> {
//                final Question item = row.getItem();
//                if (row.isHover() && item != null) {
//                    processHover(item);
//                }
//            });
//            if (! row.isEmpty()
//            && event.getButton()==MouseButton.PRIMARY
//            && event.getClickCount() == 2) {
				row.setOnMouseClicked(event -> {
						final Question item = row.getItem();
						if (event.getClickCount()==1 && !row.isEmpty()) {
								processClick(primaryStage, item);
						}
				});
				return row;
		});


//        https://blog.idrsolutions.com/2014/04/tutorial-how-to-setup-key-combinations-in-javafx/
//        https://docs.oracle.com/javafx/2/ui_controls/menu_controls.htm
		MenuBar menuBar = new MenuBar();
		Menu mainMenu = new Menu("File");
		MenuItem exitCmd = new MenuItem("Exit");
		mainMenu.getItems().addAll(exitCmd);
		menuBar.getMenus().add(mainMenu);
		exitCmd.setOnAction(new EventHandler() {
				@Override
				public void handle(Event event) {
//                primaryStage.close();

						Platform.exit();
						System.exit(0);
				}
		});
		exitCmd.setAccelerator(new KeyCodeCombination(KeyCode.Q, KeyCombination.CONTROL_DOWN));

//        StackPane root = new StackPane();
//        root.getChildren().add(menuBar);
//        root.getChildren().add(tableView);
//        root.getChildren().addAll(menuBar, tableView);

		// aktifkan scheduler
		scheduleWork();

		BorderPane root = new BorderPane();
		root.setTop(menuBar);
		root.setCenter(tableView);

		Scene scene = new Scene(root, 1200, 768);

//        https://stackoverflow.com/questions/18700478/set-row-height-in-javafx-tableview
		scene.getStylesheets().add("gaya.css");

		primaryStage.setTitle("Wieke's StackOverflow Table");
		primaryStage.setScene(scene);

//        http://www.java2s.com/Code/Java/JavaFX/GetScreensize.htm
		Rectangle2D primaryScreenBounds = Screen.getPrimary().getVisualBounds();
		primaryStage.setWidth(primaryScreenBounds.getWidth());
		lebar = primaryScreenBounds.getWidth();
		tinggi = primaryScreenBounds.getHeight();

		primaryStage.show();
	}

	private void processClick(Stage primaryStage, Question item) {
//        System.out.println("Aku harus buka ini: " + item.getAlamat());
		copyClipboard(item.getAlamat());

//        Label secondLabel = new Label("I'm a Label on new Window");
		WebView internet = new WebView();
		internet.getEngine().load(item.getAlamat());

		StackPane secondaryLayout = new StackPane();
		secondaryLayout.getChildren().add(internet);

		double lebarWindow = 0.7;
		double offset = 1-lebarWindow;
		Scene secondScene = new Scene(secondaryLayout, lebar * lebarWindow, tinggi);

		// New window (Stage)
		Stage newWindow = new Stage();
		newWindow.setTitle("Second Stage");
		newWindow.setScene(secondScene);

		// Set position of second window, related to primary window.
		newWindow.setX(primaryStage.getX() + (lebar * offset)); // jk pengen 60% lebar maka * (100-60)/100
		newWindow.setY(primaryStage.getY() + 0);

		newWindow.show();
	}

	public void addQuestions(String url, ObservableList<Question> answer) throws IOException {

		Document doc = Jsoup.connect(url).get();
		Elements divQuestion = doc.select("div.question-summary");
		for (Element question: divQuestion) {
			Element divTags = question.select("div.tags").first();
			Elements elemTags = divTags.select("a.post-tag");
			List<String> listTags = elemTags
				.stream()
				.map(elem -> elem.text())
				.collect(Collectors.toList());
			String tags = String.join(", ", listTags);

			Element user = question.select("div.user-details a").first();
			String username = user.text();

			Element waktos1 = question.selectFirst("div.user-action-time span");
			String waktos2 = waktos1.attr("title");
			String waktos3 = waktos1.text();
			String waktos = waktos2 + " " + waktos3;

			Element elemAnswered = question.selectFirst("div.stats div.status strong");
			String answered = elemAnswered.text();
			Element link = question.select("a.question-hyperlink").first();
			String pertanyaan = "(" + answered + ") " + link.text();

			Question q = new Question(username, pertanyaan, waktos, link.attr("abs:href"), tags);
			answer.add(q);
		}
	}

	ObservableList<Question> getObservableList() throws IOException {
		ObservableList<Question> answer = FXCollections.observableArrayList();

		for (int i=1; i<=Pages; i++) {
			String url = stackOverflow;
			if (i > 1) url += "?tab=newest&page=" + i;
			addQuestions(url, answer);
		}

		return answer;
	}

	ObservableList<Question> getObservableList2() throws IOException {
		ObservableList<Question> answer = FXCollections.observableArrayList();

		try {
			System.out.println("Oprekking: " + soUrl);
			URL so = new URL(soUrl);
			URLConnection conn = so.openConnection();
			InputStream is = conn.getInputStream();
			GZIPInputStream gis = new GZIPInputStream(is);
			BufferedReader br = new BufferedReader(
				new InputStreamReader(gis)
			);
			String inputLine;
			System.out.println("Sblm baca BR");
			while ((inputLine = br.readLine()) != null) {
				JSONObject job = new JSONObject(inputLine);
				System.out.println("Terima: " + job.toString());
			}
			System.out.println("Stlh baca BR");
		} catch(Exception e) {
		}

		return answer;
	}
}

--#

--% C:/work/oprek/coba/stackoverflow/javaso/src/main/resources/gaya.css
.table-row-cell {
	-fx-cell-size: 50px;
}

// https://stackoverflow.com/questions/39512621/change-javafx-tableview-font-size/39514062

.table-view .table-cell{
	-fx-font-weight:bold;
	-fx-font-size:18px;
	/* -fx-text-fill:orange; */
}

//Style of each column header in the tableView
.table-view .column-header {
		-fx-background-color: transparent;
}

//Style of each column header's background in the tableView
.table-view .column-header-background{
	-fx-background-color: linear-gradient(#131313 0.0%, #424141 100.0%);
}

//Style of each entire row in the table view when is hovered
.table-row-cell:hover {
	-fx-background-color:orange;
}

//Style of each entire row in the table view when is getting focused
.table-row-cell:focused {
	-fx-background-color:purple;
}

--#

