import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

import javax.lang.model.util.ElementScanner6;

public class Server6 extends Thread {
	private Socket concurrentSocket;

	public Server6(Socket clientSocket) {
		this.concurrentSocket = clientSocket;
	}

	public static void main(String[] args) {
		try {
			ServerSocket serverSocket = new ServerSocket(8001);
			System.out.println("Aguardando Cliente");
			while (true){
				Socket clientSocket = serverSocket.accept();
				System.out.println("Cliente conectado:"+clientSocket);
				Server6 client = new Server6(clientSocket);
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

			String nome = scanner.nextLine();
			String nivel = scanner.nextLine();
			String sala = scanner.nextLine();
			String ndepend = scanner.nextLine();
			float salariobruto = Float.parseFloat(sala);
			int depe = Integer.parseInt(ndepend);

			
			if(nivel.equals("A")){
				if(depe!=0){
					salariobruto*=0.92;
				}else{
					salariobruto*=0.97;
				}
			}else if(nivel.equals("B")){
				if(depe!=0){
					salariobruto*=0.90;
				}else{
					salariobruto*=0.95;
				}
			}else if(nivel.equals("C")){
				if(depe!=0){
					salariobruto*=0.85;
				}else{
					salariobruto*=0.92;
				}
			}else if(nivel.equals("D")){
				if(depe!=0){
					salariobruto*=0.83;
				}else{
					salariobruto*=0.90;
				}
			}else{
				out.println("Categoria inválida");
			}
			
			out.println("Funcionario: "+nome+" Nível: '"+nivel+"' Salario liquido:R$"+salariobruto);
		} catch (IOException i){}
	}

}