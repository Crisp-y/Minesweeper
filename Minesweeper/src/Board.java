import java.util.*;

public class Board {
    int rows;
    int columns;
    ArrayList<ArrayList<Tile>> board;

    public Board(int rows, int columns, int mines){
        this.rows = rows;
        this.columns = columns;
        board = new ArrayList<>(rows);
        for (int i = 0; i < rows;i++) {
            ArrayList<Tile> newRow = new ArrayList<>(columns);
            for (int j = 0; j < columns; j++) {
                newRow.add(new Tile());
            }
            board.add(newRow);
        }

    }

    private void generateMines(){

    }

    public int getRows(){ return rows;}
    public int getColumns(){ return columns;}
    public ArrayList<ArrayList<Tile>> getBoard(){ return board;}
}
