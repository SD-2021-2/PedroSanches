import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

public class Server3 extends Thread {
	private Socket concurrentSocket;

	public Server3(Socket clientSocket) {
		this.concurrentSocket = clientSocket;
	}

	public static void main(String[] args) {
		try {
			ServerSocket serverSocket = new ServerSocket(8001);
			System.out.println("Aguardando Cliente");
			while (true){
				Socket clientSocket = serverSocket.accept();
				System.out.println("Cliente conectado:"+clientSocket);
				Server3 client = new Server3(clientSocket);
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

			String sn1 = scanner.nextLine();
			String sn2 = scanner.nextLine();
			String sn3 = scanner.nextLine();


			String foi_aprovado = "Reprovado";
			int n1 = Integer.parseInt(sn1);
			int n2 = Integer.parseInt(sn2);
			int n3 = Integer.parseInt(sn3);
			float m1 = (n1+n2)/2;
			float m2 = (m1+n3)/2;

			if(m1>=7){
				foi_aprovado="Aprovado";
			}else if(m1>=3 & m2>=5 ){
				foi_aprovado="Aprovado";
			}
			
			out.println(foi_aprovado);
		} catch (IOException i){}
	}

}