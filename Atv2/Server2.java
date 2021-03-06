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
			InputStream inputStream = concurrentSocket.getInputStream();
			Scanner scanner = new Scanner(inputStream);
			OutputStream outputStream = concurrentSocket.getOutputStream();
			PrintWriter out =new PrintWriter(outputStream, true);

			String Nome = scanner.nextLine();
			String Sexo = scanner.nextLine();
			String Idade = scanner.nextLine();
			String maioridade = " É menor de idade";
			if(Sexo.equals("masculino")){
				if(Integer.parseInt(Idade)>=18){
					maioridade = " É maior de idade";
				}
			}else if(Sexo.equals("feminino")){
				if(Integer.parseInt(Idade)>=21){
					maioridade = " É maior de idade";
				}
			}
			
			out.println("A pessoa: "+Nome+maioridade);
		} catch (IOException i){}
	}

}