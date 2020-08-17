import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.println("Welcome to Minesweeper!");
        System.out.println("Loading a 7 by 7 board with 7 mines");
        Board board = new Board(7, 7, 7);
        System.out.println("Enter first click as [row] [col]");
        Scanner sc = new Scanner(System.in);
        String coords = sc.nextLine();
        Coordinate start = new Coordinate(Integer.parseInt(coords.split(" ")[0]), Integer.parseInt(coords.split(" ")[1]));
        board.generateMines(start);
    }
}
