#include <stdio.h>
#include <stdlib.h>
#include <iostream>

using namespace std;
int table[9][9], ans = 0;

bool check_x(int x, int y, int value)  //�ˬd����L����
{
    for (int i = 0; i < 9; i++) {
        if (y == i)
            continue;
        if (value == table[x][i])
            return 1;  //������
    }
    return 0;
}

bool check_y(int x, int y, int value)  //�ˬd�������L����
{
    for (int i = 0; i < 9; i++) {
        if (x == i)
            continue;
        if (value == table[i][y])
            return 1;  //������
    }
    return 0;
}

bool check_square(int x, int y, int value)  //�ˬd�b�p�E�c�椺���L����
{
    int checkx = x, checky = y, checkx3, checky3;
    for (; checkx % 3 != 0; --checkx) {
    }
    for (; checky % 3 != 0; --checky) {
    }
    checkx3 = checkx + 3;
    checky3 = checky + 3;
    for (int i = checkx; i < checkx3; i++) {
        for (int j = checky; j < checky3; j++) {
            if (y == i)
                continue;
            if (value == table[i][j])
                return 1;  //������
        }
    }
    return 0;
}

void DFS(int pos) {
    int x, y;
    x = pos / 9;
    y = pos % 9;

    if (pos == 81) {
        ans++;
        // printf("\n");
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++)
                printf("%d ", table[i][j]);
            printf("\n");
        }
        printf("\n");
        return;
    }

    if (!table[x][y]) {
        for (int i = 1; i <= 9; i++) {
            if (check_x(x, y, i))
                continue;
            if (check_y(x, y, i))
                continue;
            if (check_square(x, y, i))
                continue;
            table[x][y] = i;
            DFS(pos + 1);
        }
        table[x][y] = 0;
    } else {
        DFS(pos + 1);
    }
}

int main() {
    ans = 0;
    for (int i = 0; i < 9; i++)
        for (int j = 0; j < 9; j++)
            scanf("%d", &table[i][j]);

    DFS(0);
    printf("there are a total of %d solution(s).\n", ans);
    return 0;
}
