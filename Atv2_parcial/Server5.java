import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

public class Server5 extends Thread {
	private Socket concurrentSocket;

	public Server5(Socket clientSocket) {
		this.concurrentSocket = clientSocket;
	}

	public static void main(String[] args) {
		try {
			ServerSocket serverSocket = new ServerSocket(8001);
			System.out.println("Aguardando Cliente");
			while (true){
				Socket clientSocket = serverSocket.accept();
				System.out.println("Cliente conectado:"+clientSocket);
				Server5 client = new Server5(clientSocket);
				client.start();
			}
		} catch (IOException i){}
	}

	public void run(){
		try {
			Socket myClient = new Socket("127.0.0.1", 8002); 
			OutputStream outputStream = concurrentSocket.getOutputStream();
			PrintWriter out =new PrintWriter(outputStream, true);

			//Pegando INPUT do Client
			InputStream inputStream1 = concurrentSocket.getInputStream();
			Scanner scanner1 = new Scanner(inputStream1);
			
			String Nome = scanner1.nextLine();
			
		
			//Enviando a requisição para o DB	
			try (OutputStreamWriter outS = new OutputStreamWriter(
				myClient.getOutputStream())) {
				outS.write(Nome);
			}

			//Recebendo os dados do DB
			InputStream inputStream = myClient.getInputStream();
			Scanner scanner = new Scanner(inputStream);

			String ida = scanner.nextLine();
			String categoria;
			int idade= Integer.parseInt(ida);
			if(idade>=18){
				categoria="Maior de idade";
			}else if(idade>=14){
				categoria="Juvenil B";
			}else if(idade>=11){
				categoria="Juvenil A";
			}else if(idade>=8){
				categoria="Infantil B";
			}else if(idade>=5){
				categoria="Infantil A";
			}else{
				categoria="Não existe";
			}
			
			out.println(categoria);
		} catch (IOException i){}
	}

}