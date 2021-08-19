import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
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
			InputStream inputStream = concurrentSocket.getInputStream();
			Scanner scanner = new Scanner(inputStream);
			OutputStream outputStream = concurrentSocket.getOutputStream();
			PrintWriter out =new PrintWriter(outputStream, true);

			String Nome = scanner.nextLine();
			String Cargo = scanner.nextLine();
			String Salario = scanner.nextLine();
			float salajuste1;
			if(Cargo.equals("operador")){
				float salajuste=Float.parseFloat(Salario);
				salajuste1=(float) (salajuste*1.2);
			}else if(Cargo.equals("programador")){
				float salajuste=Float.parseFloat(Salario);
				salajuste1=(float) (salajuste*1.18);
			}else{
				float salajuste=Float.parseFloat(Salario);
				salajuste1=(float) (salajuste*1.0);
			}
			
			out.println("Nome: "+Nome+". Salario ajustado: R$"+Float.toString(salajuste1));
		} catch (IOException i){}
	}

}