import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

public class Server2 extends Thread {
	private Socket concurrentSocket;

	public Server2(Socket clientSocket) {
		this.concurrentSocket = clientSocket;
	}

	public static void main(String[] args) {
		try {
			ServerSocket serverSocket = new ServerSocket(8001);
			System.out.println("Aguardando Cliente");
			while (true){
				Socket clientSocket = serverSocket.accept();
				System.out.println("Cliente conectado:"+clientSocket);
				Server2 client = new Server2(clientSocket);
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
			//InputStream inputStream = myClient.getInputStream();
			//Scanner scanner = new Scanner(inputStream);

			//String Sexo = scanner.nextLine();
			//String Idade = scanner.nextLine();

			String Sexo = "Masculino";
			//String Sexo = Feminino;
			String Idade = "20";
			//String Idade = 19;
		
			String maioridade = " É menor de idade";

			if(Sexo.equals("Masculino")){
				if(Integer.parseInt(Idade)>=18){
					maioridade = " É maior de idade";
				}
			}else if(Sexo.equals("Feminino")){
				if(Integer.parseInt(Idade)>=21){
					maioridade = " É maior de idade";
				}
			}
			
			out.println("A pessoa: "+Nome+maioridade);
		} catch (IOException i){}
	}

}