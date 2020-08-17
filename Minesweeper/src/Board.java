import java.util.*;

public class Board {
    int rows;
    int columns;
    int mines;
    ArrayList<ArrayList<Tile>> board;

    public Board(int rows, int columns, int mines){
        this.rows = rows;
        this.columns = columns;
        this.mines = mines;
        board = new ArrayList<>(rows);
        for (int i = 0; i < rows;i++) {
            ArrayList<Tile> newRow = new ArrayList<>(columns);
            for (int j = 0; j < columns; j++) {
                newRow.add(new Tile());
            }
            board.add(newRow);
        }
    }

    public void generateMines(Coordinate start){
        ArrayList<Coordinate> coords = new ArrayList<>();
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                if (!start.equals(i, j)) {
                    coords.add(new Coordinate(i, j));
                }
            }
        }
        Random random = new Random();
        for (int i = 0; i < mines; i++){
            Coordinate newMine = coords.get(random.nextInt(coords.size()));
            board.get(newMine.getY()).get(newMine.getX()).setMine();
            //Change the count of nearby mines

        }

    }

    public int getRows(){ return rows;}
    public int getColumns(){ return columns;}
    public ArrayList<ArrayList<Tile>> getBoard(){ return board;}
    //Add a printing method for testing
}
