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

			String num1 = scanner.nextLine();
			String num2 = scanner.nextLine();
			
			int num1aux = Integer.parseInt(num1);
			int num2aux = Integer.parseInt(num2);
			Carta aux =  new Carta();

			out.println(aux.toString(num1aux,num2aux));
		} catch (IOException i){}
	}

}