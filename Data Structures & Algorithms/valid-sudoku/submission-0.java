class Solution {
    public boolean isValidSudoku(char[][] board) {
        HashMap<Integer,ArrayList<Character>> col = new HashMap<>(); //this is for coloumns
        HashMap<Integer,ArrayList<Character>> row = new HashMap<>(); //this is for row
        HashMap<Integer,ArrayList<Character>> squ = new HashMap<>(); //this is for 3 by 3 square 

for (int i=0; i<9;i++) {
    row.put(i,new ArrayList<Character>());
    col.put(i, new ArrayList<Character>());
    for (int j=0; j<9; j++) {
    squ.put((i/3)*3+(j/3),new ArrayList<Character>());
    }
}
        for (int i=0; i<9; i++) {
            
            for (int j =0; j<9; j++){
                if (board[i][j]==('.')){
                    continue;
                }
                if (row.get(i).contains(board[i][j]) || col.get(j).contains(board[i][j]) || squ.get((i/3)*3+(j/3)).contains(board[i][j])) {
                    return false;
                }
            
                row.get(i).add(board[i][j]);
                col.get(j).add(board[i][j]);
                squ.get((i/3)*3+(j/3)).add(board[i][j]);
            }
        
        }
    return true;
        
    }
}
