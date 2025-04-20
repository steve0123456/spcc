#include <stdio.h>
#include <string.h>
#include <ctype.h>

int nounCount = 1;
int tokenCount = 0;

int isVerb(const char *word) {
    return strcmp(word, "hate") == 0 || strcmp(word, "like") == 0;
}

int isKeyword(const char *word) {
    return strcmp(word, "If") == 0 || strcmp(word, "then") == 0;
}

int isActionStart(const char *word) {
    return strcmp(word, "they") == 0;
}

int isEndSymbol(const char *word) {
    return strcmp(word, ".") == 0 || strcmp(word, "$") == 0;
}

void analyzeToken(char *word) {
    // Remove punctuation attached to word
    int len = strlen(word);
    if (ispunct(word[len - 1]) && word[len - 1] != '$') {
        word[len - 1] = '\0';
    }

    if (isKeyword(word)) {
        printf("(k) ");
        tokenCount++;
    } else if (isVerb(word)) {
        printf("(v) ");
        tokenCount++;
    } else if (isActionStart(word)) {
        printf("(a) ");
        tokenCount++;
    } else if (isEndSymbol(word)) {
        printf("(op) ");
        tokenCount++;
    } else if (strlen(word) > 0) {
        printf("(n,%d) ", nounCount++);
        tokenCount++;
    }
}

int main() {
    char input[256];
    printf("Enter the input string:\n");
    fgets(input, sizeof(input), stdin);

    // Tokenize and check
    char *token = strtok(input, " \n");

    while (token != NULL) {
        // If token ends with '.' or '$', analyze them separately
        int len = strlen(token);
        if (len > 1 && (token[len - 1] == '.' || token[len - 1] == '$')) {
            char punct[2] = {token[len - 1], '\0'};
            token[len - 1] = '\0';  // Strip punctuation
            analyzeToken(token);
            analyzeToken(punct);
        } else {
            analyzeToken(token);
        }
        token = strtok(NULL, " \n");
    }

    printf("\nTotal Tokens: %d\n", tokenCount);
    return 0;
}
