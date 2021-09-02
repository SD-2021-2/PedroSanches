import java.io.*;
import java.net.*;

import java.util.Scanner;

public class Server1 extends Thread {
	private Socket concurrentSocket;

	public Server1(Socket clientSocket) {
		this.concurrentSocket = clientSocket;
	}

	public static void main(String[] args) {
		try {
			ServerSocket serverSocket = new ServerSocket(8001);
			
			System.out.println("Aguardando Cliente");
			while (true){
				Socket clientSocket = serverSocket.accept();
				System.out.println("Cliente conectado:"+clientSocket);
				Server1 client = new Server1(clientSocket);
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
			OutputStreamWriter outS = new OutputStreamWriter(myClient.getOutputStream());
			BufferedWriter bw = new BufferedWriter(outS);
			bw.write(Nome);
			bw.flush(); 
			

			//Recebendo os dados do DB
			InputStream inputStream = myClient.getInputStream();
			Scanner scanner = new Scanner(inputStream);

			String Cargo = scanner.nextLine();
			String Salario = scanner.nextLine();

			//String Cargo= "Operador";
			//String Salario= "123";
			//System.out.println(Cargo);

			float salajuste1;
			if(Cargo.equals("Operador")){
				float salajuste=Float.parseFloat(Salario);
				salajuste1=(float) (salajuste*1.2);
			}else if(Cargo.equals("Programador")){
				float salajuste=Float.parseFloat(Salario);
				salajuste1=(float) (salajuste*1.18);
			}else{
				float salajuste=Float.parseFloat(Salario);
				salajuste1=(float) (salajuste*1.0);
			}
			
			out.println("Nome: "+Nome+". Salario ajustado: R$"+Float.toString(salajuste1));
			
			bw.close();
			myClient.close();
			scanner.close();
			scanner1.close();
		} catch (IOException i){}
	}

}