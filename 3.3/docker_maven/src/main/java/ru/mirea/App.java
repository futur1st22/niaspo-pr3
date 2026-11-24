package ru.mirea;
import com.sun.net.httpserver.HttpServer;
import java.net.InetSocketAddress;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
public class App {
 public static void main(String[] args)throws Exception {
  if(args.length>0&&args[0].equals("check")){System.out.println("Java application from Maven JAR: 2 + 3 = "+(2+3));return;}
  int port=Integer.parseInt(System.getenv().getOrDefault("PORT","10000"));
  var server=HttpServer.create(new InetSocketAddress("0.0.0.0",port),0);
  server.createContext("/",exchange->{
   var result=Files.readString(Path.of("build-result.txt"));
   var version=Files.readString(Path.of("maven-version.txt"));
   String body="<!doctype html><meta charset='utf-8'><h1>Сборка Java-проекта через Maven</h1><p>Кузнецов Максим Дмитриевич, ИКБО-15-25</p><pre>"+result+"\n"+version+"</pre><p>JAR собран командой mvn package и реально запущен. Maven установлен в этом контейнере.</p>";
   byte[] data=body.getBytes(StandardCharsets.UTF_8);exchange.getResponseHeaders().set("Content-Type","text/html; charset=utf-8");exchange.sendResponseHeaders(200,data.length);exchange.getResponseBody().write(data);exchange.close();
  });
  server.start();System.out.println("Maven/JAR demonstration on "+port);
 }
}
