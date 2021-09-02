import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

public class Server4 extends Thread {
	private Socket concurrentSocket;

	public Server4(Socket clientSocket) {
		this.concurrentSocket = clientSocket;
	}

	public static void main(String[] args) {
		try {
			ServerSocket serverSocket = new ServerSocket(8001);
			System.out.println("Aguardando Cliente");
			while (true){
				Socket clientSocket = serverSocket.accept();
				System.out.println("Cliente conectado:"+clientSocket);
				Server4 client = new Server4(clientSocket);
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

			String alt = scanner.nextLine();
			String sex = scanner.nextLine();
			
			float peso;
			float altura= Float.parseFloat(alt);
			String pesof;
			if(sex.equals("masculino")){
				peso=(float) ((altura*72.7)-58);
				pesof=Float.toString(peso);
			}else if(sex.equals("feminino")){
				peso=(float) ((altura*62.1)-44.7);
				pesof=Float.toString(peso);
			}else{
				pesof=("Sexo não identificado");
			}
			
			out.println(pesof);
		} catch (IOException i){}
	}

}